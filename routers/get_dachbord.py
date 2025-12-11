from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

@router.get("/get-dashboard")
def get_names(db: Session = Depends(get_db)):
    """
    يرجع جميع الأسماء الموجودة في جدول Add
    """
    names = db.query(models.dachbord).all()  # استرجاع كل الصفوف
    result = [{"id": n.id, "pc_name ": n.pc_name , "food" : n.food ,"time" : n.time, "price" : n.price , "created_at":n.created_at} for n in names]  # تحويل لكل JSON
    return {
        "PC": result
    }
