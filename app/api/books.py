from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db import crud
from app import schemas
from app.dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Book])
def read_books(
    skip: int = 0,
    limit: int = 100,
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    db: Session = Depends(get_db)
):
    books = crud.get_books(db, skip=skip, limit=limit, category_id=category_id)
    return books

@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.post("/", response_model=schemas.Book, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    # Проверяем существование категории
    db_category = crud.get_category(db, category_id=book.category_id)
    if db_category is None:
        raise HTTPException(status_code=400, detail="Category not found")
    return crud.create_book(db=db, book=book)

@router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    if book.category_id is not None:
        db_category = crud.get_category(db, category_id=book.category_id)
        if db_category is None:
            raise HTTPException(status_code=400, detail="Category not found")
    
    db_book = crud.update_book(db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    success = crud.delete_book(db, book_id=book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return None