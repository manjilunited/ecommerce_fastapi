from fastapi import APIRouter, HTTPException, Query
from typing import Sequence, Annotated
from fastapi import Depends 
from sqlmodel import SQLModel, create_engine, Session, select
from datetime import datetime 
from sqlmodel import SQLModel, Field
from category.models import Category
from utils.db import SessionDep 

router = APIRouter()

@router.get('/categories')
async def get_categories(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int,Query(le=100)] = 100,
  ) -> Sequence[Category]:
    categories = session.exec(select(categories).offset(offset).limit(limit)).all()
    return categories 

@router.post('/categories')
async def save_category(cat: Category, session: SessionDep) -> Category:
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat 

@router.get("/categories/{id}")
async def show_category(id: int, session: SessionDep) -> Category:
    category = session.get(Category, id)
    if not category:
        raise HTTPException(status_code=404, detail="Hero not found")
    return category 

@router.delete("/categories/{id}")
async def delete_categories(id: int, session: SessionDep):
    category = session.get(Category, id)
    if not category:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(category)
    session.commit()
    return {"ok": True}

