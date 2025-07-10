from app.models.enums_model import Examples
from app.models.customer_model import CustomerPlan
from sqlmodel import SQLModel, Field, Relationship


class PlanModel(SQLModel):
    name: str = Field(default=None)
    price: int = Field(default=None)
    description: str = Field(default=None)

class PlanCreate(PlanModel):
    model_config = {
        "json_schema_extra": {
            "examples": [Examples.PLAN.value]
        }
    }

class PlanUpdate(PlanModel):
    model_config = {
        "json_schema_extra": {
            "examples": [Examples.PLAN.value]
        }
    }


class Plan(PlanModel, table=True):
    id_plan: int | None = Field(default=None, primary_key=True)
    customers: list["Customer"] = Relationship(
        back_populates="plans",
        link_model=CustomerPlan
    )
