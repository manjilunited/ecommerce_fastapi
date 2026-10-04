from sqlmodel import Field, SQLModel

class Cart(SQLModel,table=True):
    __tablename__="carts"

    id:int=Field(default=None,primary_key=True)
    user_id:int=Field()
    quantity:int=Field()