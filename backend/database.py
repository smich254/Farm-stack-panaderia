from motor.motor_asyncio import AsyncIOMotorClient
from models import Task, UpdateTask
from bson import ObjectId
from decouple import config

import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

mongodb_url = [
    config("MONGODB_SRV")
]

client = AsyncIOMotorClient(mongodb_url)
database = client.taskdatabase
collection = database.tasks


async def get_one_task_id(id):
    task = await collection.find_one({"_id": ObjectId(id)})
    return task


async def get_one_task(title):
    task = await collection.find_one({"title": title})
    return task


async def get_all_tasks():
    tasks = []
    cursor = collection.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks


async def create_task(task):
    new_task = await collection.insert_one(task)
    created_task = await collection.find_one({"_id": new_task.inserted_id})
    return created_task


async def update_task(id: str, data: UpdateTask):
    task = {k: v for k, v in data.dict().items() if v is not None}
    await collection.update_one({"_id": ObjectId(id)}, {"$set": task})
    document = await collection.find_one({"_id": ObjectId(id)})
    return document


async def delete_task(id):
    await collection.delete_one({"_id": ObjectId(id)})
    return True