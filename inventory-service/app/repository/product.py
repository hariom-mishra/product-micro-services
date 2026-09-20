from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schema.product import Product
from app.models.product import (
    CreateProductRequestModel, 
    GetProductsRequestModel,
)

class ProductRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_products(self, data: GetProductsRequestModel):
        result = await self.db.execute(
            select(Product)
            .limit(data.limit)
            .offset(data.offset)
        )

        products = result.scalars().all()
        return products

    async def create_products(
        self, data: CreateProductRequestModel):
        try:
            product = Product(
                name = data.name,
                price = data.price,
                stock = data.stock
            )

            self.db.add(product)
            await self.db.commit()
            await self.db.refresh(product)

            return product
        
        except Exception as e:
            await self.db.rollback()
            raise e

    async def get_product_by_id(self, id: int):
        try:
            result = await self.db.execute(
                select(Product)
                .where(Product.id == id)
            )

            product = result.scalars().first()
            return product

        except Exception as e:
            await self.db.rollback()
            raise e