from sqlmodel import SQLModel


class ProductCreate(SQLModel):
    title: str
    slug: str
    description: str
    price: float
    stock_level: int


class ProductUpdate(SQLModel):
    title: str
    slug: str
    description: str
    price: float
    stock_level: int


class ProductResponse(SQLModel):
    id: int
    title: str
    slug: str
    description: str
    price: float
    stock_level: int
