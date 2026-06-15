from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
books = [
    {'title': 'не знаю', 'author': 'хз', 'year': 1922},
    {'title': 'не знаю2', 'author': 'хз2', 'year': 1934}
]
@app.get('/books')
def get_products():
    return books
@app.get('/books/{book_id}')
def get_book(book_id: int):
    return books[book_idв]
class Book(BaseModel):
    title: str
    author: str
    year: int
@app.post('/books')
def create_book(book: Book):
    books.append({'title': book.title, 'author': book.author, 'year': book.year})
    return {'message': f'{book.title} was added'}