from fastapi import APIRouter, HTTPException, Query 
from utils.db import SessionDep 
from cart.models import Cart
from sqlmodel import SQLModel, Field 
from typing import Sequence, Annotated 
from datetime import datetime 
from sqlmodel import SQLModel, create_engine, Session , select
from fastapi import Depends 
from cart.controller import (
    get_all_cart,
    get_cart_by_id,
    create_cart,
    update_cart,
    delete_cart
)
from cart.dtos import CartCreate, CartUpdate, CartResponse 


router=APIRouter()


@router.get("/cart")
def get_cart(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(gt=0, le=100)] = 100
) -> Sequence[Cart]:

    return get_all_cart(session)


@router.post("/cart")
def save_cart(
    cart: Cart,
    session: SessionDep
) -> Cart:

    return create_cart(cart, session)


@router.get("/cart/{id}")
def get_cart_item(
    id: int,
    session: SessionDep
) -> Cart:

    return get_cart_by_id(id, session)


@router.put("/cart/{id}")
def update_cart_item(
    id: int,
    updated_cart: Cart,
    session: SessionDep
) -> Cart:

    return update_cart(id, updated_cart, session)


@router.delete("/cart/{id}")
def delete_cart_item(
    id: int,
    session: SessionDep
):

    return delete_cart(id, session)