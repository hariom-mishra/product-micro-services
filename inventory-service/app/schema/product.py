from app.core.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Integer

class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primay_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Float)
    stocks: Mapped[int] = mapeed_column(Integer)