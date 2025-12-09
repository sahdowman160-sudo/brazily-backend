from pydantic import BaseModel, EmailStr
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from functools import lru_cache
from typing import List, Optional

class Add(BaseModel):
    name: str

class Time(BaseModel):
    pc_name: str
    time: str
    price: str
class OPen(BaseModel):
    pc_name: str
    time: str
    price: str
class Food(BaseModel):
    pc_name: str
    food: str
    price: str

class Dachbord(BaseModel):
    pc_name: str
    food: Optional[str] = None
    time: Optional[str] = None
    price: str