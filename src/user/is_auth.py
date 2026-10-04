from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt

from utils.db import SessionDep
from user.models import Users
from utils.helpers import get_expiration_time
from utils.settings import settings 


SECRET_KEY = "my-super-secret-key"
ALGORITHM = "HS256"

security = HTTPBearer()


def create_access_token(user_id: int, role: str):
    expire = get_expiration_time(settings.EXP_TIME)

    payload = {
        "user_id": user_id,
        "role": role
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: SessionDep = None
):

    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("user_id")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = session.get(Users, user_id)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user