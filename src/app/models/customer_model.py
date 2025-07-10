from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel


class CustomerModel(SQLModel):
    # Modelo del usuario
    name: str = Field(default=None, description="Nombre del usuario")
    description: str | None = Field(default=None, description="Informacion del usuario")
    email: str = Field(default=None, description="Correo del usuario")
    age: int = Field(default=None, description="Edad del usuario")


class CustomerCreate(CustomerModel):
    # Punto intermedio para generar el modelo del usuario a guardar en la db
    pass

class CustomerUpdate(CustomerModel):
    # Punto intermedio para actualizar la informacion del modelo usuario guardado en la db
    pass

class Customer(CustomerModel, table=True):
    # Modelo del usuario almacenado en la base de datos
    id_customer: int | None = Field(default=None, primary_key=True)
    transactions: list["Transaction"] = Relationship(back_populates='customer')
