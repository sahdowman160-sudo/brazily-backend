from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

@router.get("/get-open-sessions")
def get_names(db: Session = Depends(get_db)):
    """
    يرجع جميع الأسماء الموجودة في جدول Add
    """
    names = db.query(models.open_pc).all()  # استرجاع كل الصفوف
    result = [{"pc_name-": n.pc_name, "time ": n.time , "price" : n.price } for n in names]  # تحويل لكل JSON
    return {
        "PC": result
    }
