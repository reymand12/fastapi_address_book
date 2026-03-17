# FastAPI Address Book

## Setup

### 1. Create virtual environment
python -m venv venv

### 2. Activate environment
Windows:
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

## Run the application

uvicorn main:app --reload

Open in browser:
http://127.0.0.1:8000/docs

---

## API Endpoints

### Create Address
POST /addresses

Example:
{
  "name": "Home",
  "latitude": 14.5995,
  "longitude": 120.9842
}

---

### Get All Addresses
GET /addresses

---

### Update Address
PUT /addresses/{id}

Example:
{
  "name": "Updated Location",
  "latitude": 14.6000,
  "longitude": 120.9850
}

---

### Delete Address
DELETE /addresses/{id}

---

### Nearby Addresses
GET /addresses/nearby?lat=14.5995&lon=120.9842&distance_km=5