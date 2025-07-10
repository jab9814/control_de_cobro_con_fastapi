from sqlmodel import select
from db_sqlite import SessionDep
from fastapi import APIRouter, status, HTTPException, Query
from app.models.customer_model import Customer, CustomerPlan, StatusEnum
from app.models.plans_model import Plan, PlanCreate


router = APIRouter(tags=['Plans'])


@router.get("/list_plans", response_model=list[Plan])
async def list_plan(session: SessionDep):
    return session.exec(select(Plan)).all()

@router.post("/create_plans", response_model=Plan, status_code=status.HTTP_201_CREATED)
async def create_plan(plan_info: PlanCreate, session: SessionDep):
    new_plan = Plan.model_validate(plan_info.model_dump())
    session.add(new_plan)
    session.commit()
    session.refresh(new_plan)
    return new_plan

@router.post("/customers/{id_customer}/plans/{id_plan}", status_code=status.HTTP_201_CREATED)
async def subscribe_customer_to_plan(
        id_customer: int, 
        id_plan: int, 
        session: SessionDep, 
        plan_status: StatusEnum = Query()
    ):
    customer_db: Customer = session.get(Customer, id_customer)
    plan_db: Plan = session.get(Plan, id_plan)
    if not (plan_db or customer_db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No existe el usuario o el plan'
        )
    customer_plan_db = CustomerPlan(
        id_plan=plan_db.id_plan, 
        id_customer=customer_db.id_customer,
        status=plan_status
    )
    session.add(customer_plan_db)
    session.commit()
    session.refresh(customer_plan_db)
    return customer_plan_db


@router.get("/customer_plans/{id_customer}/plans")
async def customer_plan(
        id_customer: int, 
        session: SessionDep,
        plan_status: StatusEnum = Query()
    ):
    customer_db: Customer = session.get(Customer, id_customer)
    if not customer_db:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail='No existe el usuario')

    query = (
        select(CustomerPlan)
        .where(CustomerPlan.id_customer == id_customer)
        .where(CustomerPlan.status ==plan_status )
    )

    return session.exec(query).all()
