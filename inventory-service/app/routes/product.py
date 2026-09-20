from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.services.product import ProductService
from app.models.product import (
    CreateProductRequestModel,
    GetProductsRequestModel,
    GetProductsResponseModel,
    ProductResponseModel,
    ReserveStockRequestModel
)

router = APIRouter()

@router.post("/", response_model=ProductResponseModel, status_code=status.HTTP_201_CREATED)
async def create_product(req: CreateProductRequestModel, db: AsyncSession = Depends(get_db)):
    try:
        service = ProductService(db)
        return await service.create_product(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=GetProductsResponseModel)
async def get_products(req: GetProductsRequestModel = Depends(), db: AsyncSession = Depends(get_db)):
    try:
        service = ProductService(db)
        return await service.get_products(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{id}", response_model=ProductResponseModel)
async def get_product_by_id(id: int, db: AsyncSession = Depends(get_db)):
    try:
        service = ProductService(db)
        product = await service.get_product_by_id(id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/reserve")
async def reserve_stock(req: ReserveStockRequestModel, db: AsyncSession = Depends(get_db)):
    try:
        service = ProductService(db)
        return await service.reserve_stock(req)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        