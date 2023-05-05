from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import relationship

from core.database.connection import Base
# from core.models.mixin import TimeStamp


class Registration(Base):

    __tablename__ = "registration"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    phone_number = Column(String(100), nullable=False, unique=True)
    token = Column(String(200) ,unique=True)
    token_expired = Column(Boolean, default=False)
    user_role = relationship("UserRoles", back_populates="users", uselist=False)


class Roles(Base):
    
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    role = Column(String(50), nullable=False)
 
    
class UserRoles(Base):

    __tablename__ = "user_roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    users_id = Column(Integer, ForeignKey('registration.id'), nullable=False, primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False, primary_key=True)
    # role = relationship("Roles")
    users = relationship("Registration", back_populates="user_role", uselist=False)
    # __table_args__ = (
    #     UniqueConstraint("users_id", "role_id", name="unique_user_role"),
    # )

 