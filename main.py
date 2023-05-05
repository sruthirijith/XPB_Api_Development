import uvicorn
from fastapi import FastAPI, Depends, HTTPException, UploadFile, Form
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session


from config.base import settings
# from core.api.admin import admin_api
# from core.api.consumer import consumer_api
# from core.api.merchant import merchant_api
from core.api.users import user_api
# from core.api.super_admin import super_admin_api
from core.database.connection import get_db, get_mongo_db, Base, engine
# from core.models.models import Country, IDProofs
from core.utils import crud
# from core.api.sales_person import sales_person_api
Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_api.router)
# app.include_router(consumer_api.router)
# app.include_router(merchant_api.router)
# app.include_router(admin_api.router)
# app.include_router(sales_person_api.router)

@app.get("/")
async def home():
    return {"XPayBack APIs"}
# app.include_router(super_admin_api.router)

# @app.get("/country", tags=["Global"])
# async def country(db : Session = Depends(get_db)):
#     country_details = db.query(Country.name,Country.flag,Country.country_code,Country.currency_symbol).order_by(Country.name).all()
#     if country_details:
#         return {

#                 "detail": {
#                 "status": "Success",
#                 "status_code": 200,
#                 "data": {
#                     "status_code": 200,
#                     "status": "Success",
#                     "message": "country details",
#                     "country": country_details
#                     },
#                 "error": None
            
#                     }
#                 }
#     else:
#         raise  HTTPException(
#         status_code = 404,
#         detail = {
#             "status": "Error",
#             "status_code": 404,
#             "data": None,
#             "error": {
#                 "status_code": 404,
#                 "status": "Error",
#                 "message": "No Data to Display"
#             }
  
#             }
#        )


# @app.get("/get_id_proof_or_address_proof", tags=["Global"])
# async def get_id_proofs(db : Session = Depends(get_db)):
#     id_proofs = db.query(IDProofs.id,IDProofs.id_type).order_by(IDProofs.id).all()
#     if id_proofs:
#         return{
#             "detail": {
#             "status": "Success",
#             "status_code": 200,
#             "data": {
#                 "status_code": 200,
#                 "status": "Success",
#                 "message": "id proofs",
#                 "id_proofs" : id_proofs
#                 },
#             "error": None
        
#                 }
#         }
#     else:
#        raise  HTTPException(
#         status_code = 404,
#         detail = {
#             "status": "Error",
#             "status_code": 404,
#             "data": None,
#             "error": {
#                 "status_code": 404,
#                 "status": "Error",
#                 "message": "No Data to Display"
#             }
  
#             }
#        )
    

# if __name__ == "__main__":
#     uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)

