# FastAPI Address Book

A simple FastAPI application to create, read, update, delete, and search addresses in an SQLite database.  
The app uses FastAPI, SQLAlchemy, and SQLite. All endpoints are documented in `/docs`.

---

## Setup

### 1. Create virtual environment
Windows:

python -m venv venv

Mac/Linux:

python3 -m venv venv


### 2. Activate environment
Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate


### 3. Install dependencies
Recommended:

pip install -r requirements.txt

Optional (manual install):

pip install fastapi uvicorn sqlalchemy pydantic


---

## Run the application

uvicorn main:app --reload


- Server runs at: http://127.0.0.1:8000
- FastAPI interactive docs: http://127.0.0.1:8000/docs

> ⚡ The SQLite database (`addresses.db`) will be automatically created in the root folder if it doesn’t exist.

---

## API Endpoints

### Create Address
**POST /addresses**

Example JSON:

{
"name": "Home",
"latitude": 14.5995,
"longitude": 120.9842
}


---

### Get All Addresses
**GET /addresses**

Returns all addresses in the database.

---

### Update Address
**PUT /addresses/{id}**

Example JSON:

{
"name": "Updated Location",
"latitude": 14.6000,
"longitude": 120.9850
}


> Replace `{id}` with the ID of the address to update.

---

### Delete Address
**DELETE /addresses/{id}**

> Replace `{id}` with the ID of the address to delete.

---

### Nearby Addresses
**GET /addresses/nearby?lat=<lat>&lon=<lon>&distance_km=<distance>**

Example:

/addresses/nearby?lat=14.5995&lon=120.9842&distance_km=5


Returns addresses within a specified distance (km) from the given coordinates.

---

## Notes

- Always activate your virtual environment before running commands.  
- `.db` file is ignored in the repo — database will be created automatically.  
- All endpoints are documented in `/docs`.  
- Logs are shown in the terminal to track requests, errors, and successes.

---

## Commit History

- Meaningful commits showing step-by-step development:  
  - Initial setup  
  - Database & model creation  
  - Logging improvements  
  - Endpoint creation and testing  
  - README updates and cleanup

---

## Quick Setup Summary (5-minute run)

1. Clone repo: `git clone https://github.com/reymand12/fastapi_address_book.git && cd fastapi_address_book`  
2. Create venv: `python -m venv venv`  
3. Activate venv: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (Mac/Linux)  
4. Install deps: `pip install -r requirements.txt`  
5. Run app: `uvicorn main:app --reload`  
6. Open browser: http://127.0.0.1:8000/docs