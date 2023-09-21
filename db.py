from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey


engine = create_engine('sqlite:///flowers.db')
Base = declarative_base()
session = sessionmaker(engine)()


class Flower(Base):
    __tablename__ = "flower"
    id = Column(Integer, primary_key=True, autoincrement=True)
    flower_name = Column(String(100), nullable=False, unique=True)
    bloom_duration = Column(Integer)
    flower_planting = relationship("FlowerPlanting", back_populates="flower")
   
    def __repr__(self):
        return f'{self.flower_name}{self.bloom_duration}'


class Month(Base):
    __tablename__ = "month"
    id = Column(Integer, primary_key=True, autoincrement=True)
    month = Column(String(20), nullable=False, unique=True)
    flower_planting = relationship("FlowerPlanting", back_populates="month")
    
    def __repr__(self):
        return f'{self.month}'


class Color(Base):
    __tablename__ = "color"
    id = Column(Integer, primary_key=True, autoincrement=True)
    color = Column(String(150), nullable=False, unique=True)
    flower_planting = relationship("FlowerPlanting", back_populates="color")
  
    def __repr__(self):
        return f'{self.color}'


class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    zone = Column(String(50), nullable=False, unique=True)
    flower_planting = relationship("FlowerPlanting", back_populates="location")

    def __repr__(self):
        return f'{self.zone}'


class FlowerPlanting(Base):
    __tablename__ = "flower_planting"
    id = Column(Integer, primary_key=True, autoincrement=True)
    qty = Column(Integer, default=0)
    flower_id = Column(Integer, ForeignKey("flower.id"))
    color_id = Column(Integer, ForeignKey("color.id"))
    location_id = Column(Integer, ForeignKey("location.id"))
    month_id = Column(Integer, ForeignKey("month.id")) 
    flower = relationship("Flower", back_populates="flower_planting")
    color = relationship("Color", back_populates="flower_planting")
    location = relationship("Location", back_populates="flower_planting") 
    month = relationship("Month", back_populates="flower_planting")
    def __repr__(self):
        return f'{self.qty}'
 
   
Base.metadata.create_all(engine)
