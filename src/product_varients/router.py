from fastapi import APIRouter, HTTPException, Query 
from utils.db import SessionDep 
from product_varients.models import ProductVariant 
from sqlmodel import SQLModel, Field 
from typing import Sequence, Annotated 
from datetime import datetime 
from sqlmodel import SQLModel, create_engine, Session , select
from fastapi import Depends 
from product_varients.dtos import (ProductVariantCreate,ProductVariantUpdate,ProductVariantResponse)
from product_varients.controller import (get_all_product_variants,get_product_variant_by_id,create_product_variant,update_product_variant,delete_product_variant)






router = APIRouter()

# GET ALL PRODUCT VARIANTS
@router.get("/product_varients")
async def get_product_varients(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(gt=0, le=100)] = 100
) -> Sequence[ProductVariantResponse]:

    return get_all_product_variants(
        session,
        offset,
        limit
    )


# CREATE PRODUCT VARIANT
@router.post("/create_product_varients")
async def create_product_varients(
    variant: ProductVariantCreate,
    session: SessionDep
) -> ProductVariantResponse:

    return create_product_variant(
        variant,
        session
    )


# GET PRODUCT VARIANT BY ID
@router.get("/product_varients/{id}")
async def show_product_varient(
    id: int,
    session: SessionDep
) -> ProductVariantResponse:

    return get_product_variant_by_id(
        id,
        session
    )


# UPDATE PRODUCT VARIANT
@router.put("/product_varients/{id}")
async def update_product_varient(
    id: int,
    variant: ProductVariantUpdate,
    session: SessionDep
) -> ProductVariantResponse:

    return update_product_variant(
        id,
        variant,
        session
    )


# DELETE PRODUCT VARIANT
@router.delete("/product_varients/{id}")
async def delete_product_varient(
    id: int,
    session: SessionDep
):

    return delete_product_variant(
        id,
        session
    )