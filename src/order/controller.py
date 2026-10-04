from fastapi import HTTPException
from sqlmodel import select

from order.models import Order
from order.dtos import OrderCreate, OrderUpdate


# GET ALL ORDERS
def get_all_orders(
    session,
    offset: int = 0,
    limit: int = 100
):
    orders = session.exec(
        select(Order)
        .offset(offset)
        .limit(limit)
    ).all()

    return orders


# GET ORDER BY ID
def get_order_by_id(
    id: int,
    session
):
    order = session.get(Order, id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


# CREATE ORDER
def create_order(
    order_data: OrderCreate,
    session
):
    order = Order(
        user_id=order_data.user_id,
        amount=order_data.amount,
        order_status=order_data.order_status,
        remarks=order_data.remarks,
        cancel_reason=order_data.cancel_reason
    )

    session.add(order)
    session.commit()
    session.refresh(order)

    return order


# UPDATE ORDER
def update_order(
    id: int,
    order_data: OrderUpdate,
    session
):
    order = session.get(Order, id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    order.user_id = order_data.user_id
    order.amount = order_data.amount
    order.order_status = order_data.order_status
    order.remarks = order_data.remarks
    order.cancel_reason = order_data.cancel_reason

    session.add(order)
    session.commit()
    session.refresh(order)

    return order


# DELETE ORDER
def delete_order(
    id: int,
    session
):
    order = session.get(Order, id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    session.delete(order)
    session.commit()

    return {
        "ok": True,
        "message": "Order deleted successfully"
    }