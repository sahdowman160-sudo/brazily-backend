from fastapi import APIRouter, Depends
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sqlalchemy.orm import Session
from database import get_db
from schemas import Dachbord
import models

router = APIRouter()

@router.post("/dashboard")
def create_buy(add: Dachbord, db: Session = Depends(get_db)):

    new_buy = models.dachbord(
        pc_name=add.pc_name,
        food=add.food if add.food else None,
        price=add.price,
        time=add.time if add.time else None,
    )

    db.add(new_buy)
    db.commit()
    db.refresh(new_buy)

    return {"message": "✅ Purchase created successfully", "buy_id": new_buy.id}