from sqlmodel import SQLModel



class UserCreate(SQLModel):
    name: str
    phone: str
    billing_address: str
    shipping_address: str
    username: str
    email: str
    password: str
    role: str



class UserUpdate(SQLModel):
    name: str
    phone: str
    billing_address: str
    shipping_address: str
    username: str
    email: str
    password: str
    role: str



class UserLogin(SQLModel):
    email: str
    password: str



class UserResponse(SQLModel):
    id: int
    name: str
    phone: str
    billing_address: str
    shipping_address: str
    username: str
    email: str
    role: str
