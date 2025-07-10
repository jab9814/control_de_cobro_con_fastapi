from sqlmodel import SQLModel, Field, Relationship
from app.models.customer_model import CustomerPlan


class PlanModel(SQLModel):
    name: str = Field(default=None)
    price: int = Field(default=None)
    description: str = Field(default=None)

class PlanCreate(PlanModel):
    pass

class PlanUpdate(PlanModel):
    pass

class Plan(PlanModel, table=True):
    id_plan: int | None = Field(default=None, primary_key=True)
    customers: list["Customer"] = Relationship(
        back_populates="plans",
        link_model=CustomerPlan
    )
