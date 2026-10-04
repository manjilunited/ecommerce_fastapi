from sqlmodel import SQLModel


class CategoryCreate(SQLModel):
    title: str
    slug: str
    description: str


class CategoryUpdate(SQLModel):
    title: str
    slug: str
    description: str


class CategoryResponse(SQLModel):
    id: int
    title: str
    slug: str
    description: str