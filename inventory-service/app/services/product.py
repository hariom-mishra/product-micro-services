from app.repository.product import ProductRepo
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import (
    CreateProductRequestModel,
    GetProductsRequestModel,
    GetProductsResponseModel,
)

class ProductService:
    def __init__(self, db: AsyncSession):
        self.repo = ProductRepo(db)

    async def create_product(self, data: CreateProductRequestModel):
        return await self.repo.create_products(data)

    async def get_products(self, data: GetProductsRequestModel):
        try:
            products = await self.repo.get_products(data)

            return GetProductsResponseModel(
                products=products,
                limit=data.limit,
                offset=data.offset
            )
        except Exception as e:
            raise e
    
    async def get_product_by_id(self, id: int):
        try:
            product = await self.repo.get_product_by_id(id)
            return product
        except Exception as e:
            raise e

    


    