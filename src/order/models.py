from sqlmodel import Field, SQLModel 

class Order(SQLModel, table=True):
     __tablename__ = "orders"
    
     id: int | None = Field(default=None, primary_key=True)
     user_id :  str = Field()
     amount : int = Field()
     order_status:  str = Field()
     remarks : str = Field() 
     cancel_reason : str = Field()  