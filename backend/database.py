from motor.motor_asyncio import AsyncIOMotorClient
from models import Task
from bson import ObjectId

client = AsyncIOMotorClient('mongodb://localhost')
database = client.taskdatabase
collection = database.tasks


async def get_one_task_id(id):
    task = await collection.find_one({'_id': ObjectId(id)})
    return task


async def get_one_task(title):
    task = await collection.find_one({'title': title})
    return task


async def get_all_tasks():
    tasks = []
    cursor = collection.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks


async def create_task(task):
    new_task = await collection.insert_one(task)
    created_task = await collection.find_one({'_id': new_task.inserted_id})
    return created_task


async def update_task(id: str, data):
    task = {k:v for k, v in data.dict().items() if v is not None}
    print(task)
    await collection.update_one({'_id': ObjectId(id)}, {'$set': task})
    document = await collection.find_one({'_id': ObjectId(id)})
    return document


async def delete_task(id: str):
    await collection.delete_one({'_id': ObjectId(id)})
    return True
