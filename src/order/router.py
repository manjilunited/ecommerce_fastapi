from fastapi import APIRouter, HTTPException, Query
from typing import Sequence, Annotated
from fastapi import Depends 
from sqlmodel import SQLModel, create_engine, Session, select
from datetime import datetime 
from sqlmodel import SQLModel, Field
from order.models import Order 
from utils.db import SessionDep 
from order.dtos import (OrderCreate,OrderUpdate,OrderResponse)
from order.controller import (get_all_orders,get_order_by_id,create_order,update_order,delete_order)
    




router = APIRouter() 

# GET ALL ORDERS
@router.get("/order")
async def get_orders(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(gt=0, le=100)] = 100
) -> Sequence[OrderResponse]:

    return get_all_orders(
        session,
        offset,
        limit
    )


# CREATE ORDER
@router.post("/create_order")
async def save_order(
    order: OrderCreate,
    session: SessionDep
) -> OrderResponse:

    return create_order(
        order,
        session
    )


# GET ORDER BY ID
@router.get("/order/{id}")
async def show_order(
    id: int,
    session: SessionDep
) -> OrderResponse:

    return get_order_by_id(
        id,
        session
    )


# UPDATE ORDER
@router.put("/order/{id}")
async def edit_order(
    id: int,
    order: OrderUpdate,
    session: SessionDep
) -> OrderResponse:

    return update_order(
        id,
        order,
        session
    )


# DELETE ORDER
@router.delete("/order/{id}")
async def remove_order(
    id: int,
    session: SessionDep
):

    return delete_order(
        id,
        session
    )