from sqlalchemy import Integer, String
from core.db import Base
from sqlalchemy.orm import Mapped, mapped_column

class Order(Base):
    __table__ = "order"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(Integer, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status: Mapped[str] = mapped_column(String(10), nullable=False)