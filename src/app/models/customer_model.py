from enum import Enum
from sqlmodel import SQLModel, Field, Relationship


class StatusEnum(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class CustomerPlan(SQLModel, table=True):
    id_customer_plan: int | None = Field(default=None, primary_key=True)
    id_plan: int = Field(foreign_key="plan.id_plan")
    id_customer: int = Field(foreign_key="customer.id_customer")
    status: StatusEnum = Field(default=StatusEnum.ACTIVE)


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
    plans: list["Plan"] = Relationship(
        back_populates="customers",
        link_model=CustomerPlan
    )
