from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    name: str
    price: float
    stock: int

class CreateProductRequestModel(ProductBase):
    pass

class ProductResponseModel(ProductBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )

class ReserveStockRequestModel(BaseModel):
    product_id: int
    quantity: int

class GetProductsRequestModel(BaseModel):
    limit: int = 10
    offset: int = 0

class GetProductsResponseModel(BaseModel):
    products: list[ProductResponseModel]
    limit: int
    offset: int

