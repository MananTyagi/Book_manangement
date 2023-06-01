from fastapi import APIRouter, HTTPException
from fastapi import Depends
from .database import SessionLocal
from sqlalchemy.orm import Session
from .schemas import Response, RequestBook, UserSchema
from . import auth
from . import crud
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create", dependencies=[Depends(auth.check_admin)], tags=["book"])
async def create_book_service(request: RequestBook, db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully").dict(exclude_none=True)


@router.get("/get_all_books",  dependencies=[Depends(auth.check_active)], tags=["book"])
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _books = crud.get_book(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_books)




@router.patch("/update",dependencies=[Depends(auth.check_admin)], tags=["book"])
async def update_book(request: RequestBook, db: Session = Depends(get_db)):
    _book = crud.update_book(db, book_id=request.parameter.id, title=request.parameter.title, author=request.parameter.author ,description=request.parameter.description, price=request.parameter.price)
    return Response(status="Ok", code="200", message="Success update data", result=_book)


@router.delete("/delete",dependencies=[Depends(auth.check_admin)], tags=["book"])
async def delete_book(request: RequestBook,  db: Session = Depends(get_db)):
    crud.remove_book(db, book_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)


@router.get("/{book_id}", dependencies=[Depends(auth.check_active)], tags=["book"])
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if book is None:
        return Response(status="fail", code="404", message="Book is not found").dict(exclude_none=True)
    
    return Response(status="Ok", code="200", message="Success fetch all data", result=book)

@router.get("/sorting_price", dependencies=[Depends(auth.check_active)], tags=["book"])
async def get_books(skip: int = 0, limit: int = 1000, sort_by: str = "price_asc", db: Session = Depends(get_db)):
    print("started")
    sorted_books = crud.get_sorted_book(db, skip, limit, sort_by=sort_by)
    print(sorted_books)
    return Response(status="Ok", code="200", message="Successfully sorted all books by their price in asceding order", result=sorted_books)




@router.post("/register", tags=["user"])
def register_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = crud.get_users_by_username(db=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Account already exist! please try again with diffrent credentials")
    db_user = crud.create_user(db=db, user=user)
    # sendmail.send_mail(to=db_user.email, token=token, username=db_user.username)
    return Response(status="Ok", code="200", message="Success registered"  , result=db_user)


@router.post("/login", tags=["user"])
def login_user( form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = crud.get_users_by_username(db=db, username=form_data.username)
    if not db_user:
        raise HTTPException(
            status_code=401, detail="Not registered account! please login with register account")

    if auth.verify_password(form_data.password, db_user.hashed_password):
        token = auth.create_access_token(db_user)
        db_user.is_active = True
        db.commit()
        return {"access_token": token, "token_Type": "bearer"}
    
    raise HTTPException(status_code=401, detail="password is not valid")


# @router.get("/verify/{token}", response_class=HTMLResponse)
# def login_user(token: str, db: Session = Depends(get_db)):
#     payload = auth.verify_token(token)
#     username = payload.get("sub")
#     db_user = crud.get_users_by_username(db, username)
#     db_user.is_active = True
#     db.commit()
#     return Response(status="Ok", code="200", message="On your token activation is set to true"  , result=None)



