from fastapi import FastAPI
from app.api import books, categories
from app.db.db import engine
from app.db import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookstore API", version="1.0.0")

@app.get("/")
async def root():
    return {
        "message": "Welcome to Bookstore API",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "API is running"}

app.include_router(categories.router, prefix="/api/v1/categories", tags=["categories"])
app.include_router(books.router, prefix="/api/v1/books", tags=["books"])