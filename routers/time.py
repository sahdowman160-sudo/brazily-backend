from fastapi import APIRouter, Depends
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sqlalchemy.orm import Session
from database import get_db
from schemas import Time
import models

router = APIRouter()

@router.post("/time")
def create_buy(add: Time, db: Session = Depends(get_db)):

    new_buy = models.Time(
        pc_name=add.pc_name,
        time=add.time,
        price=add.price
    )

    db.add(new_buy)
    db.commit()
    db.refresh(new_buy)

    return {"message": "✅ Purchase created successfully", "buy_id": new_buy.id}
