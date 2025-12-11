from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

@router.get("/getPc")
def get_pcs(db: Session = Depends(get_db)):
    """
    Returns all PCs from the Add table
    """
    pcs = db.query(models.Add).all()
    result = [{"id": pc.id, "name": pc.name} for pc in pcs]
    return {"PC": result}


@router.get("/gettime")
def get_times(db: Session = Depends(get_db)):
    """
    Returns all time entries with pc_name
    """
    times = db.query(models.Time).all()
    result = [
        {
            "id": t.id, 
            "time": t.time,
            "price": t.price,
            "pc_name": t.pc_name
        } 
        for t in times
    ]
    return {"PC": result}


@router.get("/getfood")
def get_foods(db: Session = Depends(get_db)):
    """
    Returns all food entries with pc_name
    """
    foods = db.query(models.Food).all()
    result = [
        {
            "id": f.id,
            "food": f.food,
            "price": f.price,
            "pc_name": f.pc_name
        } 
        for f in foods
    ]
    return {"PC": result}


@router.post("/deltime")
def delete_time_records(db: Session = Depends(get_db)):
    """
    Deletes all time records from the Time table
    This is called automatically when countdown reaches 0
    """
    try:
        # Delete all time records
        deleted_count = db.query(models.Time).delete()
        db.commit()
        
        return {
            "success": True,
            "message": f"Successfully deleted {deleted_count} time records",
            "deleted_count": deleted_count
        }
    except Exception as e:
        db.rollback()
        return {
            "success": False,
            "message": f"Error deleting time records: {str(e)}",
            "deleted_count": 0
        }


@router.post("/reset")
def reset_all_data(db: Session = Depends(get_db)):
    """
    Deletes ALL time and food records
    This resets the entire system
    """
    try:
        # Delete all time records
        time_deleted = db.query(models.Time).delete()
        
        # Delete all food records
        food_deleted = db.query(models.Food).delete()
        
        db.commit()
        
        return {
            "success": True,
            "message": f"Successfully reset all data",
            "time_deleted": time_deleted,
            "food_deleted": food_deleted
        }
    except Exception as e:
        db.rollback()
        return {
            "success": False,
            "message": f"Error resetting data: {str(e)}",
            "time_deleted": 0,
            "food_deleted": 0
        }


@router.post("/deltime/{pc_name}")
def delete_time_by_pc(pc_name: str, db: Session = Depends(get_db)):
    """
    Deletes time records for a specific PC
    """
    try:
        deleted_count = db.query(models.Time).filter(
            models.Time.pc_name == pc_name
        ).delete()
        db.commit()
        
        return {
            "success": True,
            "message": f"Successfully deleted {deleted_count} time records for {pc_name}",
            "deleted_count": deleted_count
        }
    except Exception as e:
        db.rollback()
        return {
            "success": False,
            "message": f"Error deleting time records: {str(e)}",
            "deleted_count": 0
        }


@router.post("/delfood/{pc_name}")
def delete_food_by_pc(pc_name: str, db: Session = Depends(get_db)):
    """
    Deletes food records for a specific PC
    """
    try:
        deleted_count = db.query(models.Food).filter(
            models.Food.pc_name == pc_name
        ).delete()
        db.commit()
        
        return {
            "success": True,
            "message": f"Successfully deleted {deleted_count} food records for {pc_name}",
            "deleted_count": deleted_count
        }
    except Exception as e:
        db.rollback()
        return {
            "success": False,
            "message": f"Error deleting food records: {str(e)}",
            "deleted_count": 0
        }


@router.get("/getPc/{pc_id}")
def get_pc_by_id(pc_id: int, db: Session = Depends(get_db)):
    """
    Get a specific PC with all its time and food data
    """
    pc = db.query(models.Add).filter(models.Add.id == pc_id).first()
    if not pc:
        return {"error": "PC not found"}
    
    times = db.query(models.Time).filter(models.Time.pc_name == pc.name).all()
    foods = db.query(models.Food).filter(models.Food.pc_name == pc.name).all()
    
    total_time = sum(float(t.time) for t in times)
    total_price = sum(float(f.price) for f in foods)
    
    return {
        "id": pc.id,
        "name": pc.name,
        "total_time": total_time,
        "total_price": total_price,
        "time_entries": [{"id": t.id, "time": t.time} for t in times],
        "food_entries": [{"id": f.id, "food": f.food, "price": f.price} for f in foods]
    }


@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    """
    Get overall statistics
    """
    total_pcs = db.query(models.Add).count()
    total_time = db.query(models.Time).all()
    total_food = db.query(models.Food).all()
    
    total_hours = sum(float(t.time) for t in total_time)
    total_revenue = sum(float(f.price) for f in total_food)
    
    return {
        "total_pcs": total_pcs,
        "total_hours": total_hours,
        "total_revenue": total_revenue
    }