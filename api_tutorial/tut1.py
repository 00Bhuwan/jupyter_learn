from fastapi import FastAPI

api = FastAPI()

#simulated database
all_todo = [
    {'todo_id': 1, 'todo_name': 'Sports', 'todo_desc': 'Play football every Sunday'},
    {'todo_id': 2, 'todo_name': 'Study', 'todo_desc': 'Read FastAPI documentation'},
    {'todo_id': 3, 'todo_name': 'Shopping', 'todo_desc': 'Buy groceries for the week'},
    {'todo_id': 4, 'todo_name': 'Sing', 'todo_desc': 'Sing in nepali'},
    {'todo_id': 5, 'todo_name': 'Trekking', 'todo_desc': "Let's go to Langtang"},
]

# get, post, put, delete
@api.get("/")
def index():
    return {"message": "Hello, World!"}

# using pydantic so as to validate data input i.e. without todo_id:int the number provided in the url would be treated as string

@api.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in all_todo:
        if todo['todo_id'] == todo_id: 
            return todo
    
@api.get("/todos")
def get_todos(first: int = None):
    if first: 
        return all_todo[:first+1]
    else:
        return all_todo
    

#imperfect code
@api.post("/todos")
def create_todo(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todo) + 1
    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_desc': todo['todo_desc']
    }
    all_todo.append(new_todo)
    return new_todo

@api.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: dict):
    for todo in all_todo:
        if todo['todo_id'] == todo_id:
            todo['todo_name'] = updated_todo['todo_name']
            todo['todo_desc'] = updated_todo['todo_desc']
            return todo
    return {"message": "Todo not found"}

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in all_todo:
        if todo['todo_id'] == todo_id:
            all_todo.remove(todo)
            return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}

# http://127.0.0.1:8000/docs --> use for interactive fastapi documentation and playing with the methods