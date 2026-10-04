from fastapi import APIRouter, HTTPException, Query
from typing import Sequence, Annotated
from fastapi import Depends 
from sqlmodel import SQLModel, create_engine, Session, select
from datetime import datetime 
from sqlmodel import SQLModel, Field
from category.models import Category
from utils.db import SessionDep 
from category.dtos import (CategoryCreate,CategoryUpdate,CategoryResponse)
from category.controller import (get_all_categories,get_category_by_id,create_category,update_category,delete_category)
    




router = APIRouter()

# GET ALL CATEGORIES
@router.get("/categories")
def get_categories(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(gt=0, le=100)] = 100
) -> Sequence[CategoryResponse]:

    return get_all_categories(
        session,
        offset,
        limit
    )


# CREATE CATEGORY
@router.post("/categories")
def save_category(
    category: CategoryCreate,
    session: SessionDep
) -> CategoryResponse:

    return create_category(
        category,
        session
    )


# GET CATEGORY BY ID
@router.get("/categories/{id}")
def show_category(
    id: int,
    session: SessionDep
) -> CategoryResponse:

    return get_category_by_id(
        id,
        session
    )


# UPDATE CATEGORY
@router.put("/categories/{id}")
def edit_category(
    id: int,
    category: CategoryUpdate,
    session: SessionDep
) -> CategoryResponse:

    return update_category(
        id,
        category,
        session
    )


# DELETE CATEGORY
@router.delete("/categories/{id}")
def delete_categories(
    id: int,
    session: SessionDep
):

    return delete_category(
        id,
        session
    )