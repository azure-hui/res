from pydantic import BaseModel


class StoreItem(BaseModel):
    store_id: str
    store_name: str
    city: str
    status: str
