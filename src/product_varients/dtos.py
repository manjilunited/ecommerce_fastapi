from sqlmodel import SQLModel


class ProductVariantCreate(SQLModel):
    title: str
    slug: str
    description: str


class ProductVariantUpdate(SQLModel):
    title: str
    slug: str
    description: str


class ProductVariantResponse(SQLModel):
    id: int
    title: str
    slug: str
    description: str