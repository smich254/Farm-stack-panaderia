from motor.motor_asyncio import AsyncIOMotorClient
from models import Product, UpdateProduct
from bson import ObjectId
from decouple import config

import dns.resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

mongodb_url = [
    config("MONGODB_SRV")
]

client = AsyncIOMotorClient(mongodb_url)
database = client.productdb
collection = database.products


async def get_one_product_id(id):
    product = await collection.find_one({"_id": ObjectId(id)})
    return product


async def get_one_product(title):
    product = await collection.find_one({"title": title})
    return product


async def get_all_products():
    products = []
    cursor = collection.find({})
    async for document in cursor:
        products.append(Product(**document))
    return products


async def create_product(product):
    new_product = await collection.insert_one(product)
    created_product = await collection.find_one({"_id": new_product.inserted_id})
    return created_product


async def update_product(id: str, data: UpdateProduct):
    product = {k: v for k, v in data.dict().items() if v is not None}
    await collection.update_one({"_id": ObjectId(id)}, {"$set": product})
    document = await collection.find_one({"_id": ObjectId(id)})
    return document


async def delete_product(id):
    await collection.delete_one({"_id": ObjectId(id)})
    return True
