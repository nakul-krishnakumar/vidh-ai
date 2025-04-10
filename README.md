# BNS-RAG: Retrieval Augmented Generation System

### 🧾 About This Application

**BNS QnA Chatbot** is an AI-powered legal assistant designed to help users understand the **Bharatiya Nyaya Sanhita (BNS)** — the updated Indian Penal Code. Built using **Retrieval-Augmented Generation (RAG)** and OpenAI's powerful language models, this chatbot fetches the most relevant sections from the latest BNS documents to answer user queries with high accuracy and context awareness.

#### 🔍 Key Features:
- 📘 **BNS-Aware**: Trained on the latest Bharatiya Nyaya Sanhita files.
- 🤖 **Conversational Interface**: Ask questions in natural language.
- 📄 **Contextual Retrieval**: Uses RAG to fetch accurate, up-to-date legal references.
- ❗ **Fact-First Answers**: No hallucinations—if an answer isn’t in the context, it tells you.
- 🌐 **Streamlit Frontend**: Clean and responsive UI for a seamless chat experience.


## Tech Stack
### Frontend
- **Streamlit**: Web application framework

### Backend
- **FastAPI**: Web server
- **Langchain**: MLOps & orchestration
- **Pinecone**: Vector Database

### Models
- ```text-embedding-3-small```: for embedding text into vectors
- ```gpt 4o-mini```: LLM

### Repository Structure
```
bns-rag/
├── controllers/   # Application logic controllers
├── db/            # Database interaction components
├── frontend/      # Streamlit UI elements
├── model/         # OpenAI model setup
├── routes/        # API routes for various functions
├── temp/          # Temporary file storage
├── utils/         # Utility functions and helpers
├── .gitignore     # Git ignore file
├── main.py        # Main application entry point
└── requirements.txt # Required dependencies
```

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Git

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/nakul-krishnakumar/bns-rag.git
   cd bns-rag
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Setup environment variables:
   ```env
   OPENAI_API_KEY=your-openai-api-key
   PINECONE_API_KEY=your-pinecone-api-key
   PINECONE_INDEX_NAME=your-pinecone-index-name
   PINECONE_NAMESPACE=your-pinecone-namespace
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Launch the server:
   ```bash
   python main.py
   ```

6. Launch the application:
   ```bash
   streamlit run frontend/app.py
   ```

7. Open your browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

## Contact and Support

For questions, suggestions, or issues, please contact:
- **Developer**: Nakul Krishnakumar
- **Email**: nakulkrishnakumar86@gmail.com
- **GitHub Issues**: Submit issues through the repository's issue tracker
