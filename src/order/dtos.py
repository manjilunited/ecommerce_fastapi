from sqlmodel import SQLModel


class OrderCreate(SQLModel):
    user_id: str
    amount: int
    order_status: str
    remarks: str
    cancel_reason: str


class OrderUpdate(SQLModel):
    user_id: str
    amount: int
    order_status: str
    remarks: str
    cancel_reason: str


class OrderResponse(SQLModel):
    id: int
    user_id: str
    amount: int
    order_status: str
    remarks: str
    cancel_reason: str