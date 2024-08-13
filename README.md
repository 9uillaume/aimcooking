# aimcooking
AI-Powered Recipe Recommendation System

AIMCooking is a recipe suggestion service that leverages OpenAI's language models to generate recipe ideas based on given ingredients or cuisine types. This backend is built using FastAPI and Strawberry GraphQL.

## Features

- Query and mutate recipes and ingredients using GraphQL.
- Suggest recipes based on ingredients and cuisine using OpenAI's GPT-3.5-turbo model.

## Tech Stack

- **FastAPI**: Web framework for building APIs.
- **Strawberry**: GraphQL library for Python.
- **OpenAI API**: For generating recipe suggestions.
- **Uvicorn**: ASGI server to run the application.

## Prerequisites

- Python 3.8+
- OpenAI API key

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/aimcooking.git
   cd aimcooking
    ```

#### Backend
1. **Make sure to be in the backend folder:**

    ```bash
    cd backend
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the backend directory:
    ```bash
    cp .env.example .env
    ```

    Add your OpenAI API key:
    ```bash
    OPENAI_API_KEY=your-openai-api-key
    ```

## Running the Backend

1. **Start the FastAPI server:**

    ```bash
    cd backend
    uvicorn main:app --reload
    ```

2. **Access the GraphQL playground:**

    Open your browser and go to http://127.0.0.1:8000/graphql to start querying and mutating data.
