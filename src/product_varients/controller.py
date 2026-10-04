from fastapi import HTTPException
from sqlmodel import select

from product_varients.models import ProductVariant
from product_varients.dtos import (
    ProductVariantCreate,
    ProductVariantUpdate
)


# GET ALL PRODUCT VARIANTS
def get_all_product_variants(
    session,
    offset: int = 0,
    limit: int = 100
):
    product_variants = session.exec(
        select(ProductVariant)
        .offset(offset)
        .limit(limit)
    ).all()

    return product_variants


# GET PRODUCT VARIANT BY ID
def get_product_variant_by_id(
    id: int,
    session
):
    product_variant = session.get(ProductVariant, id)

    if not product_variant:
        raise HTTPException(
            status_code=404,
            detail="Product variant not found"
        )

    return product_variant


# CREATE PRODUCT VARIANT
def create_product_variant(
    variant_data: ProductVariantCreate,
    session
):
    product_variant = ProductVariant(
        title=variant_data.title,
        slug=variant_data.slug,
        description=variant_data.description
    )

    session.add(product_variant)
    session.commit()
    session.refresh(product_variant)

    return product_variant


# UPDATE PRODUCT VARIANT
def update_product_variant(
    id: int,
    variant_data: ProductVariantUpdate,
    session
):
    product_variant = session.get(ProductVariant, id)

    if not product_variant:
        raise HTTPException(
            status_code=404,
            detail="Product variant not found"
        )

    product_variant.title = variant_data.title
    product_variant.slug = variant_data.slug
    product_variant.description = variant_data.description

    session.add(product_variant)
    session.commit()
    session.refresh(product_variant)

    return product_variant


# DELETE PRODUCT VARIANT
def delete_product_variant(
    id: int,
    session
):
    product_variant = session.get(ProductVariant, id)

    if not product_variant:
        raise HTTPException(
            status_code=404,
            detail="Product variant not found"
        )

    session.delete(product_variant)
    session.commit()

    return {
        "ok": True,
        "message": "Product variant deleted successfully"
    }