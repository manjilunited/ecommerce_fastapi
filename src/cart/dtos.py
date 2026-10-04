from sqlmodel import SQLModel


class CartCreate(SQLModel):
    product_id: int
    quantity: int


class CartUpdate(SQLModel):
    product_id: int
    quantity: int


class CartResponse(SQLModel):
    id: int
    product_id: int
    quantity: int