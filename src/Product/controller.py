
from fastapi import HTTPException
from sqlmodel import select

from Product.models import Products
from Product.dtos import ProductCreate, ProductUpdate


# GET ALL PRODUCTS
def get_all_products(
    session,
    # offset: int = 0,
    # limit: int = 100
):
    products = session.exec(
        select(Products)
        # .offset(offset)
        # .limit(limit)
    ).all()
   
    return products


# GET PRODUCT BY ID
def get_product_by_id(
    id: int,
    session
):
    product = session.get(Products, id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# CREATE PRODUCT
def create_product(
    product_data: ProductCreate,
    session
):
    product = Products(
        title=product_data.title,
        slug=product_data.slug,
        description=product_data.description,
        price=product_data.price,
        stock_level=product_data.stock_level
    )

    session.add(product)
    session.commit()
    session.refresh(product)

    return product


# UPDATE PRODUCT
def update_product(
    id: int,
    product_data: ProductUpdate,
    session
):
    product = session.get(Products, id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product.title = product_data.title
    product.slug = product_data.slug
    product.description = product_data.description
    product.price = product_data.price
    product.stock_level = product_data.stock_level

    session.add(product)
    session.commit()
    session.refresh(product)

    return product


# DELETE PRODUCT
def delete_product(
    id: int,
    session
):
    product = session.get(Products, id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    session.delete(product)
    session.commit()

    return {
        "ok": True,
        "message": "Product deleted successfully"
    }
