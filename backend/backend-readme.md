# Pharmacy E-commerce LLM Assistant - Backend

## Overview

This repository contains the backend code for a pharmacy e-commerce assistant that leverages Large Language Models (LLMs) to provide natural language interactions with users. The system helps customers find pharmaceutical products, track orders, get product information, and provides customer support in a conversational manner.

## Features

- **Natural Language Processing**: Process user queries in natural language
- **Product Search**: Search for pharmaceutical products in the database
- **Order Tracking**: Allow users to track their orders
- **User Information**: Retrieve user profiles and purchase history
- **Security Modes**: Two security levels (SAFE/UNSAFE) to control data access
- **Content Safety**: Content moderation using LlamaGuard and PromptGuard
- **Function Calling**: Dynamic function selection based on user queries
- **Database Integration**: SQLite integration for data storage and retrieval

## Architecture

The backend is composed of several key components:

1. **FastAPI Server** (`main.py`): Provides REST API endpoints for the frontend
2. **LLM Manager** (`model.py`): Orchestrates interactions with the LLM model
3. **Safety Module** (`safety_module.py`): Ensures safe content generation
4. **Function Handlers** (`function_handlers.py`): Executes database operations

## Technical Stack

- **Python 3.8+**
- **FastAPI**: Web framework for building APIs
- **SQLite**: Database for storing e-commerce data
- **Ollama**: Local LLM service
- **Transformers**: For content safety checks
- **PyTorch**: Required for model inference
- **Pydantic**: Data validation and settings management

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/D-monstrateur-d-attaques-LLM.git
   cd D-monstrateur-d-attaques-LLM/backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup the database**:
   Ensure the SQLite database is properly set up at `../BDD/ecommerce.db`

5. **Install Ollama**:
   Follow the instructions at [Ollama website](https://ollama.ai) to install Ollama.
   
6. **Pull required models**:
   ```bash
   ollama pull llama3.1:8b-instruct-fp16
   ollama pull llama-guard3:8b
   ```

## Configuration

Modify the configuration variables in the code files if needed:
- Database paths in `model.py` and `function_handlers.py`
- Security settings in `model.py` and `main.py`
- Model names and parameters in `model.py`

## Usage

1. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   - API will be available at http://localhost:8000
   - Swagger UI documentation at http://localhost:8000/docs

## API Endpoints

- **POST /api/chat**: Send user messages and get AI responses
- **GET /api/customers**: Retrieve a list of customers

## Security Modes

The system operates in two security modes:

- **SAFE**: Enforces strict access controls, only allowing users to access their own data
- **UNSAFE**: Allows broader access to data but relies on the LLM to enforce privacy

## Development

### Understanding the Code Structure

- **model.py**: Core LLM interaction logic
- **main.py**: FastAPI server and endpoints
- **safety_module.py**: Content moderation components
- **function_handlers.py**: Database function handlers

### Adding New Features

To add new functions to the LLM:
1. Add the function definition to `function_handlers.py`
2. Register the function in the `_get_tools` method in `model.py`
3. Implement both SAFE and UNSAFE versions of the function

## License

[Your License Information]

## Contributors

[Your Name and Contributors]
