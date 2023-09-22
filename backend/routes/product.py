from fastapi import APIRouter, HTTPException
from database import (
    get_all_products,
    get_one_product,
    get_one_product_id,
    create_product,
    update_product,
    delete_product
)
from models import Product, UpdateProduct

product = APIRouter()


@product.get("/ping")
def welcome():
    return {"message": "Welcome to the API!"}


@product.get('/api/products')
async def get_products():
    response = await get_all_products()
    return response


@product.get('/api/products/{id}', response_model=Product)
async def get_product(id: str):
    response = await get_one_product_id(id)
    if response:
        return response
    raise HTTPException(404, f"There is no product with the id {id}")


@product.post('/api/products', response_model=Product)
async def save_product(product: Product):
    productFound = await get_one_product(product.title)
    if productFound:
        raise HTTPException(409, "Product already exists")

    response = await create_product(product.dict())
    print(response)
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@product.put('/api/products/{id}', response_model=Product)
async def put_product(id: str, data: UpdateProduct):
    response = await update_product(id, data)
    if response:
        return response
    raise HTTPException(404, f"There is no product with the id {id}")


@product.delete('/api/products/{id}')
async def remove_product(id: str):
    response = await delete_product(id)
    if response:
        return "Successfully deleted product"
    raise HTTPException(404, f"There is no product with the id {id}")
