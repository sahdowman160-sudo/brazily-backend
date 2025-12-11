from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

@router.post("/decrease_time")
def decrease_time(db: Session = Depends(get_db)):
    """
    تقليل دقيقة واحدة من كل جهاز
    """
    time_entries = db.query(models.Time).all()
    for entry in time_entries:
        # تقليل دقيقة واحدة (1/60 ساعة)
        entry.time = max(entry.time - (1/60), 0)
        db.add(entry)
    db.commit()
    return {"status": "success", "message": "Time decreased for all PCs"}
