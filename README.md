# D-monstrateur-d-attaques-LLM

# Pharmacy E-commerce LLM Assistant Framework

## Overview

This repository contains a complete framework for a pharmacy e-commerce assistant powered by Large Language Models (LLMs). The system provides natural language interactions for users to search products, track orders, retrieve information, and receive customer support in a conversational manner.

The project demonstrates both the capabilities and potential security vulnerabilities of LLM-powered applications, including a specialized component for security testing and prompt injection attack demonstration.

## Repository Structure

This project is organized into several key components:

### 1. Backend (`/backend`)

The core server application that processes user requests, interacts with the LLM, and handles database operations.

- **Technology**: Python, FastAPI, SQLite, Ollama
- **Key Features**: 
  - LLM integration with function calling
  - Security modes (SAFE/UNSAFE)
  - Content safety checking
  - Database operations

### 2. Frontend Interface (`/llm-interface`)

The user interface for interacting with the LLM assistant.

- **Technology**: React.js, Bootstrap
- **Key Features**:
  - Interactive chat interface
  - User selection
  - Security mode toggle
  - Debug panel

### 3. Database (`/BDD`)

SQLite database containing pharmaceutical product data, user information, orders, and other e-commerce data.

### 4. Penetration Testing (`/pharma_pentest`)

Tools for security testing and demonstrating prompt injection vulnerabilities.

- **Technology**: Python, ZenGuard framework adapter
- **Key Features**:
  - Prompt injection attack testing
  - Security mode comparison
  - Visualization and reporting

## Getting Started

### Prerequisites

- Python 3.8+ for backend and testing components
- Node.js and npm for frontend
- Ollama for local LLM hosting

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/D-monstrateur-d-attaques-LLM.git
   cd D-monstrateur-d-attaques-LLM
   ```

2. **Set up the backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Set up the LLM**:
   Install Ollama following instructions at [Ollama website](https://ollama.ai).
   Pull the required models:
   ```bash
   ollama pull llama3.1:8b-instruct-fp16
   ollama pull llama-guard3:8b
   ```

4. **Set up the frontend**:
   ```bash
   cd ../llm-interface
   npm install
   ```

5. **Set up the penetration testing tools** (optional):
   ```bash
   cd ../pharma_pentest
   pip install -r requirements.txt
   ```

### Running the System

1. **Start the backend server**:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

2. **Start the frontend application**:
   ```bash
   cd llm-interface
   npm start
   ```

3. **Access the application**:
   Open your browser and navigate to [http://localhost:3000](http://localhost:3000)

4. **Run security tests** (optional):
   ```bash
   cd pharma_pentest
   python run_pentest.py
   ```

## Security Modes

The system demonstrates two security approaches:

- **SAFE Mode**: Function-level security controls that filter sensitive data
- **UNSAFE Mode**: Relies on the LLM to enforce privacy and security boundaries

This dual-mode approach allows for comparative analysis of different security strategies in LLM-powered applications.

## Project Purpose

This project serves as:

1. A functional demonstration of LLM integration in e-commerce
2. An educational tool for understanding LLM security vulnerabilities
3. A framework for testing prompt injection defense strategies

## License



## Contributors

Fayza Sidi Cheikh
Valentin Choserot
