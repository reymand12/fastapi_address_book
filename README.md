# FastAPI Address Book

## Install dependencies
pip install fastapi uvicorn sqlalchemy pydantic

## Run app
uvicorn main:app --reload

## Endpoints
- POST /addresses
- GET /addresses
- PUT /addresses/{id}
- DELETE /addresses/{id}
- GET /addresses/nearby?lat=&lon=&distance_km=