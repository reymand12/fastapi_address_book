from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from db import init_db, get_db, Address
from pydantic import BaseModel
import math
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI()

# Initialize DB (ONLY here)
init_db()

# Pydantic model for input validation
class AddressInput(BaseModel):
    name: str
    latitude: float
    longitude: float

# --- CRUD Endpoints ---

# Create address
@app.post("/addresses")
def create_address(address: AddressInput, db: Session = Depends(get_db)):
    logger.info(f"Creating address: {address.name}")

    db_address = Address(
        name=address.name,
        latitude=address.latitude,
        longitude=address.longitude
    )
    db.add(db_address)
    db.commit()
    db.refresh(db_address)

    logger.info(f"Address created with ID: {db_address.id}")
    return db_address

# Get all addresses
@app.get("/addresses")
def get_addresses(db: Session = Depends(get_db)):
    logger.info("Fetching all addresses")
    return db.query(Address).all()

# Update address
@app.put("/addresses/{address_id}")
def update_address(address_id: int, address: AddressInput, db: Session = Depends(get_db)):
    logger.info(f"Updating address ID: {address_id}")

    db_address = db.query(Address).filter(Address.id == address_id).first()
    if not db_address:
        logger.error("Address not found")
        raise HTTPException(status_code=404, detail="Address not found")

    db_address.name = address.name
    db_address.latitude = address.latitude
    db_address.longitude = address.longitude
    db.commit()
    db.refresh(db_address)

    logger.info("Address updated successfully")
    return db_address

# Delete address
@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting address ID: {address_id}")

    db_address = db.query(Address).filter(Address.id == address_id).first()
    if not db_address:
        logger.error("Address not found")
        raise HTTPException(status_code=404, detail="Address not found")

    db.delete(db_address)
    db.commit()

    logger.info("Address deleted")
    return {"message": "Address deleted"}

# --- Nearby addresses endpoint ---

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

@app.get("/addresses/nearby")
def get_nearby(lat: float, lon: float, distance_km: float, db: Session = Depends(get_db)):
    logger.info(f"Searching nearby addresses within {distance_km} km")

    results = []
    for addr in db.query(Address).all():
        if haversine(lat, lon, addr.latitude, addr.longitude) <= distance_km:
            results.append(addr)

    logger.info(f"Found {len(results)} nearby addresses")
    return results