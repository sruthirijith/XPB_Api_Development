from typing import Optional, Text

from pydantic import BaseModel, EmailStr, Field


class UsersBase(BaseModel):
    full_name: str = Field(..., max_length=100, description="Full name")
    email: EmailStr = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=200, description="Password")
    phone_number: str = Field(..., min_length=5, max_length=20, description="Phone number")
    
    class Config:
        orm_mode = True

        
# class UserRoles(BaseModel):
#     role: str = Field(..., min_length=1, max_length=20, description="User role")
#     description: str = Field(..., min_length=5, max_length=500, description="User role description")
    
#     class Config:
#         orm_mode = True


class UserCreate(UsersBase):
    role_id: int
    
    class Config:
        orm_mode = True


# class Users(BaseModel):
#     full_name : Optional[str]
#     email : Optional[EmailStr]
#     password : Optional[str]
#     phone_number : Optional[str]


# class LoginSchema_email(BaseModel):

#    email : Optional[EmailStr]


# class PhoneNumberLoginSchema(BaseModel):

#     phone_number : str


# class Otp(BaseModel):
#     otp : str
#     key : Optional[str]
#     phone_number : str


# class UserOut(BaseModel):
#     full_name: str = Field(..., max_length=100, description="Full name")
#     email: EmailStr = Field(..., description="user email")
#     phone_number: str = Field(..., min_length=5, max_length=20, description="Phone number")


# class Change_pin(BaseModel):
#     old_pin : str = Field(..., max_length = 200, description = "Existing pin")
#     new_pin : str = Field(..., max_length = 200, description = "New pin")
#     reenter_pin :str = Field(..., max_length = 200, description = "Reenter pin")


# class Change_password(BaseModel):
#     old_password: str = Field(..., max_length=200, description="Existing Password")
#     new_password: str = Field(..., max_length=200, description="New Password")
#     reenter_password: str = Field(..., max_length=200, description="Reenter Password")


# class Add_Pin(BaseModel):
#     pin : str
#     reenter_pin : str


# class GenerateOtp(BaseModel):
#     phone_number: str
#     channel: Optional[str]


# class VerifyOtp(BaseModel):
#     phone_number: str
#     otp: str

# class LoginSchemaEmailPass(BaseModel):
#     email : str
#     password : str

# class reset_password(BaseModel):
#     token : str
#     password : str