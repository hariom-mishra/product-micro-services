from sqlalchemy.ext.asyncio import AsyncSession
from app.models.order import OrderRequest
from sqlalchemy import select, update
from app.schema.order import Order
class OrderRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_order(self, data: OrderRequest):
        try:
            order = Order(
                product_id=data.product_id,
                quantity=data.quantity,
                status="Placed"
            )
            db.add(order)
            await db.commit()
            await db.refresh(order)
            return order
        except Exception as e:
            raise e