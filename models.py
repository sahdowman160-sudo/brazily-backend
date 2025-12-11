from sqlalchemy import Column, Integer, String , Float ,JSON , Text ,DateTime
from database import Base , engine
from datetime import datetime
from sqlalchemy.orm import relationship

class Add(Base):
    __tablename__ = "PS"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

class Time(Base):
    __tablename__ = "time"

    id = Column(Integer, primary_key=True, index=True)
    pc_name = Column(String(50))
    time = Column(Float)
    price = Column(String(50))
    
class Food(Base):
    __tablename__ = "food"

    id = Column(Integer, primary_key=True, index=True)
    pc_name = Column(String(50))
    food = Column(String(50))
    price = Column(String(50))

class dachbord(Base):
    __tablename__ = "dachbord"
    
    id = Column(Integer, primary_key=True, index=True)
    pc_name = Column(String(50), nullable=False)
    food = Column(String(50), nullable=True)  # Make it optional
    time = Column(String(50), nullable=True)  # Make it optional
    price = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow) 

class open_pc(Base):
    __tablename__ = "open_pc"
    
    id = Column(Integer, primary_key=True, index=True)
    pc_name = Column(String(50))
    time = Column(String(50))  # Make it optional
    price = Column(String(50))





Base.metadata.create_all(bind=engine)
