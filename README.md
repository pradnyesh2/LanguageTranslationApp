# Language Translation App

A simple, yet powerful language translation application built with a modern Python stack, leveraging the capabilities of large language models for accurate and efficient translations. This project demonstrates how to integrate LangChain for orchestrating LLM calls, Groq for fast inference, and LangServe with FastAPI for building a robust and scalable API.

## ✨ Features

* **Real-time Translation:** Translate text between various languages instantly.

* **Leverages LLMs:** Utilizes advanced large language models for high-quality translations.

* **Fast Inference with Groq:** Achieves rapid translation speeds thanks to Groq's optimized hardware.

* **Scalable API:** Built with FastAPI and LangServe for easy deployment and consumption.

* **Extensible:** Designed to be easily extendable to support more languages or custom translation logic.

## 🚀 Technologies Used

* **Python:** The core programming language.

* **LangChain:** A framework for developing applications powered by language models. It helps in chaining together different components to build complex LLM workflows.

* **Groq:** A specialized hardware and software platform designed for accelerated LLM inference, providing incredibly fast response times.

* **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

* **LangServe:** A library for deploying LangChain runnables as a REST API, making it easy to serve your LLM applications.

* **Uvicorn:** An ASGI web server for running FastAPI applications.

## 🛠️ Setup Instructions

Follow these steps to get the project up and running on your local machine.

### Prerequisites

* Python 3.9+

* `pip` (Python package installer)

### 1. Clone the Repository


### 2. Create a Virtual Environment (Recommended)
conda create -p venv python==3.12 -y
conda activate venv/

### 3. Install Dependencies
pip install -r requirements.txt
python-dotenv
ipykernel
langchain_community
langchain_core
langchain_openai
langchain_groq
sse_starlette
streamlit
pydantic<2.0.0
fastapi<0.100.0
langchain
langserve==0.0.18
uvicorn
httpx>=0.24.1,<0.27

### 4. Configure Environment Variables
Create a `.env` file in the root directory of your project and add your Groq API key:
GROQ_API_KEY="your_groq_api_key_here"

ou can obtain a Groq API key from [Groq Cloud](https://console.groq.com/keys).

## 💡 Usage
### 1. Run the Application

Start the FastAPI application:
python serve.py
OR
uvicorn serve:app --reload --port 8000

This will start the server at `http://127.0.0.1:8000`. The `--reload` flag enables auto-reloading on code changes, which is useful for development.

### 2. Use the API

You can interact with the translation API using tools like `curl`, Postman, or by writing client-side code.

## 🌐 API Endpoints

The application exposes the following API endpoint for translation:

### `POST /chain/invoke`

Translates text from a English to a target language.

* **URL:** `http://127.0.0.1:8000/translate/invoke`

* **Method:** `POST`

* **Headers:**

  * `Content-Type: application/json`

* **Request Body (JSON):**
{
  "input": {
    "language": "string",
    "text": "string"
  },
  "config": {},
  "kwargs": {}
}

* **URL:** `http://127.0.0.1:8000/docs`

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

1. Fork the repository.

2. Create a new branch (`git checkout -b feature/your-feature-name`).

3. Make your changes.

4. Commit your changes (`git commit -m 'Add new feature'`).

5. Push to the branch (`git push origin feature/your-feature-name`).

6. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License.
