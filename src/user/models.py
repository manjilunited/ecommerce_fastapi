from sqlmodel import Field, SQLModel 

class Users(SQLModel, table = True): 
    __tablename__ = "users"

    id : int | None = Field(default=None, primary_key=True)
    name : str = Field()
    phone : str = Field()
    billing_address : str = Field()
    shipping_address : str = Field()
    username : str = Field()
    email : str = Field()
    password : str = Field()
    role : str = Field() 
   

