from sqlmodel import Field, SQLModel


class Products(SQLModel, table=True):
    __tablename__ = "products"

    id: int | None = Field(default=None, primary_key=True)

    title: str = Field()
    slug: str = Field()
    description: str = Field()

    price: float = Field()
    stock_level: int = Field(default=0) 