from fastapi import APIRouter, Depends
from app.core.db import get_db
from app.models.order import OrderRequest

router = APIRouter(prefix="order", tags=["order"])

@router.post("/")
async def order_product(req: OrderRequest, db= Depends(get_db)):
    pass