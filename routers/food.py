from fastapi import APIRouter, Depends
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sqlalchemy.orm import Session
from database import get_db
from schemas import Food
import models

router = APIRouter()

@router.post("/food")
def create_buy(add: Food, db: Session = Depends(get_db)):

    new_buy = models.Food(
        pc_name=add.pc_name,
        food=add.food,
        price=add.price
    )

    db.add(new_buy)
    db.commit()
    db.refresh(new_buy)

    return {"message": "✅ Purchase created successfully", "buy_id": new_buy.id}
