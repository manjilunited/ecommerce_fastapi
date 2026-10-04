from fastapi import HTTPException
from sqlmodel import select

from cart.models import Cart 
from cart.dtos import CartCreate, CartUpdate



# GET ALL CART ITEMS
def get_all_cart(session):
    cart = session.exec(
        select(Cart)
    ).all()

    return cart


# GET CART ITEM BY ID
def get_cart_by_id(
    id: int,
    session
):
    cart = session.get(Cart, id)

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found"
        )

    return cart


# ADD ITEM TO CART
def create_cart(
    cart: Cart,
    session
):
    session.add(cart)
    session.commit()
    session.refresh(cart)

    return cart


# UPDATE CART ITEM
def update_cart(
    id: int,
    updated_cart: Cart,
    session
):
    cart = session.get(Cart, id)

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found"
        )

    cart.product_id = updated_cart.product_id
    cart.quantity = updated_cart.quantity

    session.add(cart)
    session.commit()
    session.refresh(cart)

    return cart


# DELETE CART ITEM
def delete_cart(
    id: int,
    session
):
    cart = session.get(Cart, id)

    if not cart:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found"
        )

    session.delete(cart)
    session.commit()

    return {
        "message": "Cart item deleted successfully"
    }