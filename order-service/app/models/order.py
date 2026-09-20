from pydantic import BaseModel, ConfigDict

class OrderBase(BaseModel):
    product_id: int
    quantity: int

class OrderResponse(OrderBase):
    id: int
    status: str

    model_config = ConfigDict()

class OrderRequest(OrderBase):
    pass