from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas

Base.metadata.create_all(engine)

app = FastAPI()
# create a db instance to talk to the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"app_name": "todo app"}

@app.get("/todos/", response_model=list[schemas.ToDo])
def get_all_todo(db: Session = Depends(get_db)):
    todo_list = db.query(models.ToDo).all()
    return todo_list


@app.post("/todo/", response_model=schemas.ToDo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    todo_db = models.ToDo(task = todo.task)
    db.add(todo_db)
    db.commit()
    db.refresh(todo_db)
    return todo_db

@app.get("/todo/{id}", response_model=schemas.ToDo)
def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.ToDo).get(id)
    return todo

@app.put("/todo/{id}", response_model=schemas.ToDo)
def update_todo(id: int, task: str, db: Session = Depends(get_db)):
    todo = db.query(models.ToDo).get(id)
    if todo:
        todo.task = task
        db.commit()
    return todo
    

@app.delete("/todo/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.ToDo).get(id)
    if todo:
        db.delete(todo)
        db.commit()
    return None


