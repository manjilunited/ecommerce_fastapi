
from fastapi import HTTPException
from sqlmodel import select

from user.models import Users
from user.dtos import UserCreate, UserUpdate, UserLogin
from user.is_auth import create_access_token


# GET ALL USERS
def get_all_users(
    session,
    offset: int = 0,
    limit: int = 100
):
    users = session.exec(
        select(Users)
        .offset(offset)
        .limit(limit)
    ).all()

    return users


# GET USER BY ID
def get_user_by_id(
    id: int,
    session
):
    user = session.get(Users, id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# REGISTER USER
def register_user(
    user_data: UserCreate,
    session
):
    # Check email
    existing_user = session.exec(
        select(Users).where(
            Users.email == user_data.email
        )
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=422,
            detail="Email already registered."
        )

    
    existing_user = session.exec(
        select(Users).where(
            Users.username == user_data.username
        )
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=422,
            detail="Username already registered."
        )

    
    user = Users(
        name=user_data.name,
        phone=user_data.phone,
        billing_address=user_data.billing_address,
        shipping_address=user_data.shipping_address,
        username=user_data.username,
        email=user_data.email,
        password=user_data.password,
        role=user_data.role
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user


# UPDATE USER
def update_user(
    id: int,
    user_data: UserUpdate,
    session
):
    existing_user = session.get(Users, id)

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    existing_user.name = user_data.name
    existing_user.phone = user_data.phone
    existing_user.billing_address = user_data.billing_address
    existing_user.shipping_address = user_data.shipping_address
    existing_user.username = user_data.username
    existing_user.email = user_data.email
    existing_user.password = user_data.password
    existing_user.role = user_data.role

    session.add(existing_user)
    session.commit()
    session.refresh(existing_user)

    return existing_user


# DELETE USER
def delete_user(
    id: int,
    session
):
    user = session.get(Users, id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    session.delete(user)
    session.commit()

    return {
        "ok": True,
        "message": "User deleted successfully"
    }


# LOGIN USER
def login_user(
    login_data: UserLogin,
    session
):
    existing_user = session.exec(
        select(Users).where(
            Users.email == login_data.email
        )
    ).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if existing_user.password != login_data.password:
        raise HTTPException(
            status_code=401,
            detail="Incorrect password"
        )

    return {
        "message": "Login successfully",
        "user": existing_user
    }
