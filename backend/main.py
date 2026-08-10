from fastapi import FastAPI
from pydantic import BaseModel

class DocumentCreate(BaseModel):
    # id: int
    title: str
    description: str
    
class UserCreate(BaseModel):
    name: str
    email: str
    age: int
app = FastAPI()


@app.get("/")
def root():
    return {"message": "DocMind AI API is running"}


@app.get("/health")
def healthy():
    return {"status": "healthy"}

@app.get("/about")
def about():
    return {
  "name": "DocMind AI",
  "version": "1.0.0",
  "description": "AI-powered document intelligence platform"
}


@app.get("/documents/{document_id}")
def get_document(document_id: int):
    return {"document_id": document_id} 

@app.get("/documents")
def list_documents(status: str | None = None):
    return {
        "status": status
    }


@app.post("/documents")
def create_document(document: DocumentCreate):
    return {
        "title": document.title,
        "description": document.description
    }
    
@app.post("/users")
def create_user(user: UserCreate):
    return {
        "name": user.name,
        "email": user.email,
        "age": user.age
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/documents/search")
def search_documents(query: str | None = None):
    return {"query": query}


@app.get("/documents/limit")
def search_documents( limit: int | None = None,offset: int | None = None):
    return { "limit": limit, "offset": offset} 