from fastapi import FastAPI
from routes.task import task

app = FastAPI()


@app.get('/')
def welcome():
    return {'message': 'Holi boli'}


app.include_router(task)
