# models/pipfs_model.py
from pydantic import BaseModel

class Pipfs(BaseModel):
    id: int
    name: str
    description: str
    # ...
