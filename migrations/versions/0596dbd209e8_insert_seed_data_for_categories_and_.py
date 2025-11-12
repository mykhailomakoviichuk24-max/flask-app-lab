"""Insert seed data for categories and products

Revision ID: 0596dbd209e8
Revises: 4c7394bbbf81  <-- (Переконайтеся, що 'Revises' правильний)
Create Date: ...
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


revision = '0596dbd209e8'
down_revision = '4c7394bbbf81' 
branch_labels = None
depends_on = None


def upgrade():
    

    
    op.execute("""
        INSERT INTO categories (name) VALUES
        ('Electronics'),
        ('Books'),
        ('Clothing'),
        ('Smartphones')
        ON CONFLICT(name) DO NOTHING
    """)

    
    op.execute("""
        INSERT INTO products (name, price, active, category_id)
        VALUES
        (
            'Samsung Galaxy', 
            899.99, 
            1,  -- '1' означає 'True' для SQLite
            (SELECT id FROM categories WHERE name = 'Smartphones')
        ),
        (
            'Google Pixel', 
            799.99, 
            1, 
            (SELECT id FROM categories WHERE name = 'Smartphones')
        )
    """)
    


def downgrade():
    
    op.execute("DELETE FROM products WHERE name IN ('Samsung Galaxy', 'Google Pixel')")
    op.execute("DELETE FROM categories WHERE name IN ('Electronics', 'Books', 'Clothing', 'Smartphones')")
    