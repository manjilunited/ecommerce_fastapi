from fastapi import APIRouter, HTTPException , Query 
from utils.db import SessionDep 
from Product.models import Products 
from sqlmodel import SQLModel, Field 
from typing import Sequence, Annotated 
from datetime import datetime 
from sqlmodel import SQLModel, create_engine, Session , select
from fastapi import Depends 
from Product.dtos import (ProductCreate,ProductResponse,ProductUpdate)
from Product.controller import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product
)    






router = APIRouter()

# GET ALL PRODUCTS
@router.get("/products/")
async def get_products(
    session: SessionDep,
    # offset: int = 0,
    # limit: Annotated[int, Query(gt=0, le=100)] = 100
) -> Sequence[ProductResponse]:

    return get_all_products(
        session,
        # offset,
        # limit
    )


# CREATE PRODUCT
@router.post("/products/")
async def save_product(
    product: ProductCreate,
    session: SessionDep
) -> ProductResponse:

    return create_product(
        product,
        session
    )


# GET PRODUCT BY ID
@router.get("/products/{id}")
async def show_product(
    id: int,
    session: SessionDep
) -> ProductResponse:

    return get_product_by_id(
        id,
        session
    )


# UPDATE PRODUCT
@router.put("/products/{id}")
async def edit_product(
    id: int,
    product: ProductUpdate,
    session: SessionDep
) -> ProductResponse:

    return update_product(
        id,
        product,
        session
    )


# DELETE PRODUCT
@router.delete("/products/{id}")
async def remove_product(
    id: int,
    session: SessionDep
):

    return delete_product(
        id,
        session
    )