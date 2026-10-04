from fastapi import APIRouter, HTTPException , Query, status
from utils.db import SessionDep 
from user.models import Users   
from sqlmodel import SQLModel, Field 
from typing import Sequence, Annotated 
from datetime import datetime 
from sqlmodel import SQLModel, create_engine, Session , select
from fastapi import Depends 
from sqlalchemy.exc import NoResultFound
from user.dtos import (UserCreate,UserUpdate,UserLogin,UserResponse)
from user.controller import (
    get_all_users,
    get_user_by_id,
    register_user,
    update_user,
    delete_user,
    login_user
) 
from user.is_auth import get_current_user



router = APIRouter() 

# GET ALL USERS
@router.get("/user/")
async def get_users(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(gt=0, le=100)] = 100
) -> Sequence[UserResponse]:

    return get_all_users(
        session,
        offset,
        limit
    )


# REGISTER
@router.post("/user_register")
def create_user(
    user: UserCreate,
    session: SessionDep
) -> UserResponse:

    return register_user(
        user,
        session
    )


# GET USER BY ID
@router.get("/users/{id}")
def get_user(
    id: int,
    session: SessionDep
) -> UserResponse:

    return get_user_by_id(
        id,
        session
    )


# UPDATE USER
@router.put("/user/{id}")
def edit_user(
    id: int,
    user: UserUpdate,
    session: SessionDep
) -> UserResponse:

    return update_user(
        id,
        user,
        session
    )


# DELETE USER
@router.delete("/user/{id}")
def remove_user(
    id: int,
    session: SessionDep
):

    return delete_user(
        id,
        session
    )


# LOGIN
@router.post("/user_login")
def login(
    user: UserLogin,
    session: SessionDep
):

    return login_user(
        user,
        session
    )


# PROTECTED PROFILE
@router.get("/my-profile")
def my_profile(
    current_user: Users = Depends(get_current_user)
):

    return current_user  