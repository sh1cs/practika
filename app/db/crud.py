from sqlalchemy.orm import Session
from . import models

def create_category(db: Session, name: str):
    new_category = models.Category(name=name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_category(db: Session, cat_id: int):
    return db.query(models.Category).filter(models.Category.id == cat_id).first()

def get_all_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def get_category_by_name(db: Session, name: str):
    return db.query(models.Category).filter(models.Category.name == name).first()

def update_category(db: Session, cat_id: int, new_name: str):
    category = db.query(models.Category).filter(models.Category.id == cat_id).first()
    if category:
        category.name = new_name
        db.commit()
        db.refresh(category)
    return category

def delete_category(db: Session, cat_id: int):
    category = db.query(models.Category).filter(models.Category.id == cat_id).first()
    if category:
        db.delete(category)
        db.commit()
    return category

def create_book(db: Session, title: str, desc: str, price: float, cat_id: int, url: str = ""):
    new_book = models.Book(
        title=title,
        description=desc,
        price=price,
        category_id=cat_id,
        url=url
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_all_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_books_by_category(db: Session, cat_id: int):
    return db.query(models.Book).filter(models.Book.category_id == cat_id).all()

def update_book(db: Session, book_id: int, **kwargs):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        for key, value in kwargs.items():
            if hasattr(book, key) and value is not None:
                setattr(book, key, value)
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book

def search_books(db: Session, term: str):
    return db.query(models.Book).filter(
        (models.Book.title.ilike(f"%{term}%")) | 
        (models.Book.description.ilike(f"%{term}%"))
    ).all()