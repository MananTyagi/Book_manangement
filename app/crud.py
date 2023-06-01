from sqlalchemy.orm import Session
from .models import Book , UserModel
from .schemas import BookSchema , UserSchema
from . import auth




def get_book(db: Session, skip: int = 0, limit: int = 100):
    re=db.query(Book).offset(skip).limit(limit).all()
    print(re)
    return db.query(Book).offset(skip).limit(limit).all()

def get_sorted_book(db: Session, skip: int = 0, limit: int = 100, sort_by: str="price_asc"):
    query = db.query(Book).offset(skip).limit(limit)
    print("started")
    if sort_by == "price_desc":
        query = query.order_by(Book.price.desc())
    elif sort_by == "price_asc":
        query = query.order_by(Book.price.asc())
    elif sort_by == "title":
        query = query.order_by(Book.title)
    else:
        query = query.order_by(Book.id)
    print(query)
    return query.all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, book: BookSchema):
    _book = Book(title=book.title, author=book.author, description=book.description)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book


def remove_book(db: Session, book_id: int):
    _book = get_book_by_id(db=db, book_id=book_id)
    db.delete(_book)
    db.commit()


def update_book(db: Session, book_id: int, title: str,author:str, description: str, price: int):
    _book = get_book_by_id(db=db, book_id=book_id)

    _book.title = title
    _book.author = author
    _book.description = description
    _book.price = price

    db.commit()
    db.refresh(_book)
    return _book


def create_user(db: Session, user: UserSchema):
    hashed_password = auth.get_password_hash(user.password)
    db_user = UserModel(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        role=user.role.value,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first() 