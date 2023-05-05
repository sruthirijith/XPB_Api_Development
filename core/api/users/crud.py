import gridfs
import phonenumbers
import random
import hashlib
import datetime


from bson.objectid import ObjectId
from fastapi.security import OAuth2PasswordBearer
from hashids import Hashids
from sqlalchemy import and_
from sqlalchemy.orm import Session, load_only
from passlib.context import CryptContext


from config.base import settings
from core.api.users import models, schema
# from core.api.consumer.models import FollowedSocialMedia
from core.database.connection import get_db
from core.utils import password, time


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user_email_login")
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
secret = settings.JWT_SECRET_KEY
ALGORITHM = settings.ALGORITHM



def create_user(db: Session, user: schema.UserCreate):
    hashed_password = password.get_hashed_password(password=user.password)
    db_user = models.Registration(
        full_name=user.full_name,
        email=user.email,
        password=hashed_password,
        phone_number=user.phone_number,
        
    )


def  get_user_by_email(db: Session, email: str):
    return db.query(models.Registration).options(load_only(
            "id", "full_name", "email", "phone_number"
        )).filter(models.Registration.email == email).first()


# def get_user_by_username(db: Session, full_name: str):
#     return db.query(models.Registration).options(load_only(
#             "id", "full_name", "email", "phone_number", "referral_code", "referred_by", "blocked", 
#             "deleted", "created_at", "updated_at"
#         )).filter(models.Users.full_name == full_name).first()


def get_user_by_phonenumber(db: Session, phone_number: str):
    return db.query(models.Registration).options(load_only(
            "id", "full_name", "email", "phone_number", 
        )).filter(models.Registration.phone_number == phone_number).first()


# def get_user_by_id(db: Session, user_id: int):
#     return db.query(models.Users).options(load_only(
#             "id", "full_name", "email", "phone_number", "referral_code", "referred_by", "blocked", 
#             "deleted", "created_at", "updated_at"
#         )).filter(models.Users.id == user_id).first()


# def validate_phone_number(phone_number: str, country_code: str) -> bool:
#     try:
#         if country_code:
#             phone_number_obj = phonenumbers.parse(phone_number, country_code)
#         else:
#             phone_number_obj = phonenumbers.parse(phone_number)
#     except phonenumbers.phonenumberutil.NumberParseException:
#         return False
#     if not phonenumbers.is_valid_number(phone_number_obj):
#         return False
#     return True

# def verify_password(password: str, hashed_pass: str) -> bool:
#     return password_context.verify(password, hashed_pass)

# def verify_email_password(db:Session , email:str ,password:str):
#     userinfo = db.query(models.Users).filter(models.Users.email==email).first()
#     verify_pass=verify_password(password,userinfo.password)

#     if  verify_pass:
#         return userinfo
        
#     else:
#         return None

def md5_encrypt():
    str2hash = datetime.datetime.now()
    md5hash = str(str2hash)+str(random.randint(0,10000))
    result = hashlib.md5(md5hash.encode())
    return (result.hexdigest())

def get_user_by_token(db : Session,token : str):
    return (
        db.query(models.Registration).filter(models.Registration.token == token).first()
    )

def update_pin(db : Session, email : str, pin : str):
    db.query(models.Registration).filter(models.Registration.email == email).update({"pin": pin})
    db.commit()
    return True

def update_change_password(db : Session, email : str, password : str):
    db.query(models.Registration).filter(models.Registration.email == email).update({"password": password})
    db.commit()
    return True

def update_token(db : Session, email : str, token : str):
    db.query(models.Registration).filter(models.Registration.email == email).update({"token" : token, "token_expired" : False})
    db.commit()
    return True

def update_reset_password(db : Session, token : str, password : str):
    db.query(models.Registration).filter(models.Registration.token == token).update({"password" : password,"token_expired" : True})
    db.commit()
    return True

# def get_user_by_email_with_pin(db: Session, email: str):
#     return db.query(models.Registration).options(load_only(
#             "id", "full_name", "email", "phone_number","pin", 
#         )).filter(models.Users.email == email).first()

# def get_user_by_email_with_password(db: Session, email: str):
#     return db.query(models.Users).options(load_only(
#             "id", "full_name", "email", "phone_number","password", 
#         )).filter(models.Users.email == email).first()

def get_user_roles(db : Session, users_id : int, role : int):
    return db.query(models.UserRoles).filter(and_(models.UserRoles.users_id==users_id , models.UserRoles.role_id==role)).first()

def add_new_role(db : Session, users_id : int, role : int):
    db_roles = models.UserRoles(
        users_id = users_id,
        role_id = role
    )
    db.add(db_roles)
    db.commit()
    db.refresh(db_roles)
    return(db_roles)

# def save_file(mongo_db , collection : str, file_name: str, content : bytes, content_type : str):
#     try:
#         fs = gridfs.GridFS(mongo_db, collection)
#         stored = fs.put(content, filename=file_name, contentType=content_type)
#         return stored
#     except Exception as e:
#         print(e)
#         return False

# def check_if_file_exists(mongo_db, collection : str, file_id : str):
#     try:
#         fs = gridfs.GridFS(mongo_db, collection)
#         exists = fs.exists(ObjectId(file_id))
#         if not exists:
#             return False
#         return True
#     except Exception as e:
#         print(e)

# def retrieve_file(mongo_db, collection : str, file_id : str):
#     try:
#         fs = gridfs.GridFS(mongo_db, collection)
#         result = fs.get(ObjectId(file_id)).read()
#         return result
#     except Exception as e:
#         print(e)
#         return False

# def delete_file(mongo_db, collection : str, file_id : str):
#     try:
#         fs = gridfs.GridFS(mongo_db, collection)
#         fs.delete(ObjectId(file_id))
#         return True
#     except Exception as e:
#         print(e)
#         return False

# def check_pin(db : Session, pin : str):
#     return db.query(models.Users).filter(models.Users.pin == pin).first()