from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.order import OrderRepo
from app.models.order import OrderRequest

class OrderService:
    def __init__(self, db: AsyncSession):
        self.reso = OrderRepo(db)

    async def order_product(self, data: OrderRequest):
        pass