from pydantic import BaseModel


class RoleSchema(BaseModel):
    id: str
    name: str
    zh_name: str

    class Config:
        from_attributes = True