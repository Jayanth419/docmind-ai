from fastapi import FastAPI

from app.database.connection import Base, engine
from app.database.models import Document,User
from app.routes.documents import router as documents_router
from app.routes.users import router as users_router
from app.routes.auth import router as auth_router

print("Registered tables:", Base.metadata.tables.keys())
print("Database URL:", engine.url)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DocMind AI",
    version="0.1.0",
    description="AI-powered document intelligence API"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to DocMind AI"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

app.include_router(users_router)

app.include_router(documents_router)
app.include_router(auth_router)