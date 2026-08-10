from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "DocMind AI API is running"}


@app.get("/healthy")
def healthy():
    return {"status": "healthy"}

@app.get("/about")
def about():
    return {
  "name": "DocMind AI",
  "version": "1.0.0",
  "description": "AI-powered document intelligence platform"
}


@app.post("/documents")
def create_document():
    return {"message": "Document Received"} 