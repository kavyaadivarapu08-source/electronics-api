from sqlalchemy import Column, Integer, String
from database import Base



class Laptop(Base):
    __tablename__ = "laptops"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(100), nullable=False)
    processor = Column(String(50), nullable=False)
    ram = Column(String(20), nullable=False)
    price = Column(Integer, nullable=False)



class Mobile(Base):
    __tablename__ = "mobiles"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(100), nullable=False)
    storage = Column(String(20), nullable=False)
    color = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False)



class Watch(Base):
    __tablename__ = "watches"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(100), nullable=False)
    type = Column(String(30), nullable=False)
    color = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False)



class TV(Base):
    __tablename__ = "tvs"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), nullable=False)
    screen_size = Column(String(20), nullable=False)
    display_type = Column(String(50), nullable=False)
    resolution = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False)



class Headphone(Base):
    __tablename__ = "headphones"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(100), nullable=False)
    type = Column(String(30), nullable=False)
    connectivity = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False)