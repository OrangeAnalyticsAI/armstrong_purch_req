from sqlalchemy import create_engine, Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class PurchaseRequisition(Base):
    __tablename__ = 'purchase_requisitions'
    
    id = Column(Integer, primary_key=True)
    item_no = Column(Integer, nullable=False)
    quantity = Column(Float, nullable=False)
    description = Column(String(150), nullable=False)
    ln_number = Column(String(50), nullable=True)
    length_mm = Column(Float, nullable=True)
    drilling_detail = Column(String(255), nullable=True)
    assembly_time = Column(Float, nullable=True)
    weight_kg = Column(Float, nullable=True)
    comments = Column(String(500), nullable=True)
    comments2 = Column(String(500), nullable=True)
    
    # Will be used in Step 3
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=True)
    production_order_id = Column(Integer, ForeignKey('production_orders.id'), nullable=True) 