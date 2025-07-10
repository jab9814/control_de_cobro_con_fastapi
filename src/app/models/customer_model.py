from db_sqlite import engine
from pydantic import EmailStr, field_validator
from sqlmodel import SQLModel, Field, Relationship, Session, select
from app.models.enums_model import Examples, StatusEnum


class CustomerPlan(SQLModel, table=True):
    id_customer_plan: int | None = Field(default=None, primary_key=True)
    id_plan: int = Field(foreign_key="plan.id_plan")
    id_customer: int = Field(foreign_key="customer.id_customer")
    status: StatusEnum = Field(default=StatusEnum.ACTIVE)


class CustomerModel(SQLModel):
    # Modelo del usuario
    name: str = Field(default=None, description="Nombre del usuario")
    description: str | None = Field(default=None, description="Informacion del usuario")
    email: EmailStr = Field(default=None, description="Correo del usuario")
    age: int = Field(default=None, description="Edad del usuario")

    @field_validator('name')
    def validate_name(cls, name: str):
        if any(char.isdigit() for char in name):
            raise ValueError("El nombre no puede contener digitos")
        return  name

    @field_validator('age')
    def validate_age(cls, age: int):
        if age < 18:
            raise ValueError("El usuario debe ser mayor a 18 anhos")
        return age

    @field_validator('email')
    def validate_email_in_db(cls, email: EmailStr):
        if Session(engine).exec(select(Customer).where(Customer.email == email)).first():
            raise ValueError("Un usuario ya cuenta con este correo")
        return email
    

class CustomerCreate(CustomerModel):
    model_config = {
        "json_schema_extra": {
            "examples": [Examples.CUSTOMER.value]
        }
    }

class CustomerUpdate(CustomerModel):
    model_config = {
        "json_schema_extra": {
            "examples": [Examples.CUSTOMER.value]
        }
    }

class Customer(CustomerModel, table=True):
    # Modelo del usuario almacenado en la base de datos
    id_customer: int | None = Field(default=None, primary_key=True)
    transactions: list["Transaction"] = Relationship(back_populates='customer')
    plans: list["Plan"] = Relationship(
        back_populates="customers",
        link_model=CustomerPlan
    )
