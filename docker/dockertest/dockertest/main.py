from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class TodoItem(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory store for the to-do items
todos = []

@app.post("/todos/", response_model=TodoItem)
def create_todo_item(todo: TodoItem):
    todos.append(todo)
    return todo

@app.get("/todos/", response_model=List[TodoItem])
def read_todo_items():
    return todos

@app.get("/todos/{todo_id}", response_model=TodoItem)
def read_todo_item(todo_id: int):
    todo = next((todo for todo in todos if todo.id == todo_id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="To-do item not found")
    return todo

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo_item(todo_id: int, updated_todo: TodoItem):
    index = next((index for index, todo in enumerate(todos) if todo.id == todo_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="To-do item not found")
    todos[index] = updated_todo
    return updated_todo

@app.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int):
    index = next((index for index, todo in enumerate(todos) if todo.id == todo_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="To-do item not found")
    todos.pop(index)
    return {"message": "To-do item deleted successfully"}
