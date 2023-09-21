from fastapi import FastAPI
from database import get_all_tasks, create_task
from models import Task

app = FastAPI()


@app.get('/')
def welcome():
    return {'message': 'Holi boli'}


@app.get('/api/tasks')
async def get_tasks():
    tasks = await get_all_tasks()
    return tasks


@app.post('/api/tasks')
async def save_task(task: Task):
    response = await create_task(task.dict())
    print(response)
    return 'create task'


@app.get('/api/tasks/{id}')
async def get_task():
    return 'single task'


@app.put('/api/tasks/{id}')
async def update_task():
    return 'updating task'


@app.delete('/api/tasks/{id}')
async def delete_task():
    return 'delete tasks'
