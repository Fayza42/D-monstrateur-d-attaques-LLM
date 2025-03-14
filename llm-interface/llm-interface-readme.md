# Pharmacy E-commerce LLM Assistant - Frontend

This repository contains the frontend interface for the Pharmacy E-commerce LLM Assistant. It provides a user-friendly chat interface for interacting with the LLM backend.

## Quick Start

### Prerequisites

- Node.js (v14 or higher)
- npm (v6 or higher)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/D-monstrateur-d-attaques-LLM.git
   cd D-monstrateur-d-attaques-LLM/llm-interface
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm start
   ```

4. **Access the application**:
   Open your browser and navigate to [http://localhost:3000](http://localhost:3000)

## Features

- Interactive chat interface for communicating with the LLM
- User selection dropdown
- Security mode toggle (SAFE/UNSAFE)
- Real-time message display
- Responsive design for mobile and desktop

## Configuration

The frontend is pre-configured to connect to the backend API at `http://localhost:8000`. If your backend is running on a different URL, you'll need to update the API endpoint in the code.

## Connecting to Backend

Make sure the backend server is running before starting the frontend application. See the backend repository README for instructions on setting up and running the backend.

## Development

- Built with React.js
- Uses Bootstrap and custom CSS for styling
- State management with React hooks
