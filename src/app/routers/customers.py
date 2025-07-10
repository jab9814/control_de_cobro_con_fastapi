from sqlmodel import select
from db_sqlite import SessionDep
from fastapi import APIRouter, status, HTTPException
from app.models.customer_model import (
    Customer,
    CustomerCreate,
    CustomerUpdate, 
) 


router = APIRouter(tags=['customers'])


@router.get("/list_customer", response_model=list[Customer])
async def list_customer(session: SessionDep):
    return session.exec(select(Customer)).all()


@router.post("/create_customers", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer(customer_info: CustomerCreate, session: SessionDep):
    new_customer = Customer.model_validate(customer_info.model_dump())
    session.add(new_customer)
    session.commit()
    session.refresh(new_customer)
    return new_customer


@router.get("/read_customer/{id_customer}", response_model=Customer)
async def read_customer(id_customer: int, session: SessionDep):
    customer_db: Customer = session.get(Customer, id_customer)
    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no existe"
        )
    return customer_db


@router.delete("/delete_customer/{id_customer}")
async def delete_customer(id_customer: int, session: SessionDep):
    customer_db: Customer = session.get(Customer, id_customer)
    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no existe"
        )
    session.delete(customer_db)
    session.commit()
    return {
        'id_customer': id_customer,
        'detail': 'ok',
    }


@router.patch("/update_customer/{id_customer}", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def update_customer(id_customer: int, customer_info: CustomerUpdate, session: SessionDep):
    customer_db: Customer = session.get(Customer, id_customer)
    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no existe"
        )
    customer_info_dict = customer_info.model_dump(exclude_unset=True)
    customer_db.sqlmodel_update(customer_info_dict)
    session.add(customer_db)
    session.commit()
    session.refresh(customer_db)
    return customer_db
