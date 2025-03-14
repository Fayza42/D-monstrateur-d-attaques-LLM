# backend/main.py
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime
from model import LLMManager, DebugInfo
import sys
from pathlib import Path
import logging
from sqlalchemy import create_engine, text
from contextlib import contextmanager
import json

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration des chemins
project_root = Path(__file__).parent.parent
db_path = project_root / "BDD/ecommerce.db"
db_url = f"sqlite:///{db_path}"

# Création du moteur SQLAlchemy
engine = create_engine(db_url)

# Initialisation des managers
llm_manager = LLMManager()

# Configuration
config = {
    "db_path": db_path,
    "db_url": db_url,
    "project_root": project_root
}


# Context manager pour la base de données
@contextmanager
def get_db():
    """Context manager pour la connexion à la base de données"""
    try:
        connection = engine.connect()
        yield connection
    finally:
        connection.close()


# Modèles Pydantic
class ChatMessage(BaseModel):
    type: str
    content: str
    timestamp: str
    sqlResults: Optional[Dict[str, Any]] = None
    debug: Optional[Dict[str, Any]] = None  # Nouveau champ pour les infos de débogage


class User(BaseModel):
    id: str
    first_name: str
    last_name: str


class ChatRequest(BaseModel):
    message: str
    template_type: Optional[str] = "sales"
    user: User
    security_mode: Optional[str] = "SAFE"
    debug: Optional[bool] = False  # Nouveau champ pour activer le débogage


# Initialisation de FastAPI
app = FastAPI(title="Pharma E-commerce Assistant API")

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/customers")
async def get_customers():
    """Récupère la liste des clients"""
    try:
        query = """
        SELECT 
            id,
            first_name,
            last_name,
            email,
            created_at,
            COALESCE(
                (SELECT SUM(total_amount) 
                FROM orders 
                WHERE customer_id = customers.id), 
                0
            ) as total_spent
        FROM customers
        ORDER BY first_name, last_name
        """

        with get_db() as conn:
            result = conn.execute(text(query))
            customers = [
                {
                    "id": str(row.id),  # Conversion en string pour JSON
                    "first_name": row.first_name,
                    "last_name": row.last_name,
                    "email": row.email,
                    "created_at": row.created_at,
                    "total_spent": float(row.total_spent)  # Conversion en float pour JSON
                }
                for row in result
            ]

        return customers
    except Exception as e:
        logger.error(f"Error fetching customers: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching customers: {str(e)}"
        )


@app.post("/api/chat")
async def chat(request: ChatRequest):
    """Endpoint de chat avec support authentification, mode sécurité et débogage"""
    try:
        # Vérification des paramètres
        if not request.user:
            raise HTTPException(
                status_code=400,
                detail="User information is required"
            )

        # Configuration du mode de sécurité si spécifié
        if request.security_mode:
            llm_manager.set_security_mode(request.security_mode)

        # Activer le mode débogage si demandé
        if request.debug:
            llm_manager.set_debug_mode(True)
        else:
            llm_manager.set_debug_mode(False)

        # Génération de la réponse
        ai_response, debug_info = llm_manager.generate_response(
            prompt=request.message,
            user_id=f"{request.user.first_name} {request.user.last_name}",
            template_type=request.template_type
        )

        # Préparer la réponse
        response = ChatMessage(
            type="assistant",
            content=ai_response,
            timestamp=datetime.now().isoformat()
        )

        # Ajouter les informations de débogage si demandé
        if request.debug and debug_info:
            response.debug = debug_info.dict()

        return response
    except Exception as e:
        logger.error(f"Chat error: {e}")

        # En cas d'erreur, créer une réponse d'erreur avec debug si nécessaire
        error_response = ChatMessage(
            type="assistant",
            content=f"Une erreur s'est produite: {str(e)}",
            timestamp=datetime.now().isoformat()
        )

        if request.debug:
            from model import LogEntry
            debug = DebugInfo()
            debug.executionLogs.append(
                LogEntry(type="error", message=f"Erreur serveur: {str(e)}")
            )
            error_response.debug = debug.dict()

        return error_response