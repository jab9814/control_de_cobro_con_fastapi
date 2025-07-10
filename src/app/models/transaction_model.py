from sqlmodel import SQLModel, Field, Relationship
from app.models.customer_model import Customer


class TransactionModel(SQLModel):
    amount: int = Field(default=None, description="Costo de la operacion")
    description: str = Field(default=None, description="Informacion de la operacion")


class TransactionCreate(TransactionModel):
    id_customer: int = Field(foreign_key="customer.id_customer")
    pass


class TransactionUpdate(TransactionModel):
    id_customer: int = Field(foreign_key="customer.id_customer")
    pass


class Transaction(TransactionModel, table=True):
    id_transaction: int | None = Field(default=None, primary_key=True)
    id_customer: int = Field(foreign_key="customer.id_customer")
    customer: Customer = Relationship(back_populates='transactions')