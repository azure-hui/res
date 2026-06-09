from typing import Literal, Optional
from pydantic import BaseModel


UserRole = Literal["owner", "store_manager"]


class UserMeData(BaseModel):
    id: int
    username: str
    full_name: Optional[str] = None
    role: UserRole