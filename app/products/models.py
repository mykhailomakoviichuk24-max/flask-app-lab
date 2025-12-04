from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
# Додаємо 'Boolean', 'DateTime' та 'func'
from sqlalchemy import Integer, String, Float, ForeignKey, Boolean, DateTime, func 
from datetime import datetime

#
# --- Клас 'Category' (без змін) ---
#
class Category(db.Model):
    __tablename__ = 'categories'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    products: Mapped[list["Product"]] = relationship(back_populates="category")

    def __repr__(self):
        return f'<Category {self.name}>'

#
# --- ОНОВЛЕНИЙ КЛАС 'Product' ---
#
class Product(db.Model):
    __tablename__ = 'products' 
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Зв'язок з Частини 2
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=True)
    category: Mapped["Category"] = relationship(back_populates="products")
    
    # Поле з Частини 4
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default='True')
    
    #
    # --- ДОДАЙТЕ ЦЕ ПОЛЕ (Частина 6) ---
    #
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now() # <-- Використовуємо SQL-функцію
    )
    # -----------------------------------

    def __repr__(self):
        return f'<Product {self.name}>'