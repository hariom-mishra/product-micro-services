from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.schema.product import Product
from app.models.product import (
    CreateProductRequestModel, 
    GetProductsRequestModel,
    ReserveStockRequestModel
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

    async def get_product_count(self, id: int):
        try:
            result = await self.db.execute(
                select(Product.stock)
                .where(Product.id == id)
            )

            product_stock = result.scalars().first()
            return product_stock
        
        except Exception as e:
            await self.db.rollback()
            raise e

    async def reserve_stock(self, data: ReserveStockRequestModel):
        try:
            result = await self.db.execute(
                update(Product)
                .where(
                    Product.id == data.product_id,
                    Product.stock >= data.quantity
                    )
                .values(
                    stock = Product.stock - data.quantity
                )
                .returning(Product)
            )

            product = result.one_or_none()
            if(product is None):
                raise HTTPException(
                    status_code=400,
                    detail="Insufficient stock"
                )

            await self.db.commit()
            return product
        except Exception as e:
            await self.db.rollback()
            raise e
        

    