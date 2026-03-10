from fastapi import FastAPI
from pydantic import BaseModel

from scripts.step8_rag_answer import get_rag_answer

# Create FastAPI app
app = FastAPI(
    title="RAG FAQ API",
    description="RAG system using Supabase vector database and OpenAI",
    version="1.0.0"
)


# Request schema
class QuestionRequest(BaseModel):
    question: str


# Response schema
class AnswerResponse(BaseModel):
    answer: str


# Root endpoint (optional but useful)
@app.get("/")
def root():
    return {"message": "RAG API is running"}


# Main RAG endpoint
@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    answer = get_rag_answer(request.question)
    return {"answer": answer}
