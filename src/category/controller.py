from fastapi import HTTPException
from sqlmodel import select

from category.models import Category
from category.dtos import CategoryCreate, CategoryUpdate


def get_all_categories(session, offset: int = 0, limit: int = 100):
    categories = session.exec(
        select(Category)
        .offset(offset)
        .limit(limit)
    ).all()

    return categories


def get_category_by_id(id: int, session):
    category = session.get(Category, id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


def create_category(category_data: CategoryCreate, session):
    category = Category(
        title=category_data.title,
        slug=category_data.slug,
        description=category_data.description
    )

    session.add(category)
    session.commit()
    session.refresh(category)

    return category


def update_category(
    id: int,
    category_data: CategoryUpdate,
    session
):
    category = session.get(Category, id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    category.title = category_data.title
    category.slug = category_data.slug
    category.description = category_data.description

    session.add(category)
    session.commit()
    session.refresh(category)

    return category


def delete_category(id: int, session):
    category = session.get(Category, id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    session.delete(category)
    session.commit()

    return {
        "message": "Category deleted successfully"
    }