from sqlmodel import Field, SQLModel


class ProductVariant(SQLModel, table = True):
    __tablename__ = "product_variants"

    id: int | None = Field(default=None, primary_key=True)
    title: str = Field()
    slug: str = Field()
    description: str = Field()