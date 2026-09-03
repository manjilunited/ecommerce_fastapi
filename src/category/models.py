from sqlmodel import Field, SQLModel

class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: int | None = Field(default=None, primary_key=True)
    title: str = Field()
    slug: str = Field()
    description: str = Field()