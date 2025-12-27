from pydantic import BaseModel, HttpUrl
from typing import Optional

class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    
    class Config:
        from_attributes = True

class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    url: HttpUrl
    category_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    url: Optional[HttpUrl] = None
    category_id: Optional[int] = None

class Book(BookBase):
    id: int
    
    class Config:
        from_attributes = True