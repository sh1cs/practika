import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import SessionLocal
from app.db.crud import get_all_categories, get_all_books, get_books_by_category

def show_data():
    db = SessionLocal()
    
    try:
        print("=" * 60)
        print("DATA FROM OCTAGON_DB")
        print("=" * 60)
        
        categories = get_all_categories(db)
        
        if not categories:
            print("No categories found.")
            return
        
        print(f"\nCategories found: {len(categories)}\n")
        
        for cat in categories:
            print(f"\n{'─' * 50}")
            print(f"CATEGORY: {cat.name} (ID: {cat.id})")
            print(f"{'─' * 50}")
            
            books = get_books_by_category(db, cat.id)
            
            if books:
                print(f"Books in category: {len(books)}")
                print(f"\n{'─' * 50}")
                print(f"{'Title':<25} {'Price':<10} {'Description'}")
                print(f"{'─' * 50}")
                
                for book in books:
                    short_desc = (book.description[:40] + '...') if book.description and len(book.description) > 40 else book.description
                    print(f"{book.title:<25} {book.price:<10.2f} {short_desc or 'No description'}")
            else:
                print("No books in this category.")
        
        print(f"\n{'=' * 60}")
        print("SUMMARY")
        print(f"{'=' * 60}")
        
        all_books = get_all_books(db)
        total_price = sum(book.price for book in all_books)
        avg_price = total_price / len(all_books) if all_books else 0
        
        print(f"Total books: {len(all_books)}")
        print(f"Total price: {total_price:.2f}")
        print(f"Average price: {avg_price:.2f}")
        
        books_no_url = [book for book in all_books if not book.url or book.url.strip() == ""]
        if books_no_url:
            print(f"\nBooks without URL:")
            for book in books_no_url:
                print(f"  - {book.title}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    show_data()
    print(f"\n{'=' * 60}")
    print("Commands:")
    print("1. Init DB: python3 app/init_db.py")
    print("2. Run app: python3 app/main.py")
    print(f"{'=' * 60}")