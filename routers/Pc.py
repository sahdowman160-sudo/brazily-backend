from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

@router.get("/Pc")
def get_names(db: Session = Depends(get_db)):
    """
    يرجع جميع الأسماء الموجودة في جدول Add
    """
    names = db.query(models.Add).all()  # استرجاع كل الصفوف
    result = [{"id": n.id, "name": n.name} for n in names]  # تحويل لكل JSON
    return {
        "PC": result
    }
