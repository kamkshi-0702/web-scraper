from pydantic import BaseModel

class UserBase(BaseModel):
    login: str
    url: str
    type: str

class UserCreate(UserBase):
    id: int

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True