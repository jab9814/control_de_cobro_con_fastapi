from sqlmodel import select
from fastapi import APIRouter, status, HTTPException
from db_sqlite import SessionDep
from app.models.customer_model import Customer
from app.models.transaction_model import (
    Transaction,
    TransactionCreate,
    TransactionUpdate,
)


router = APIRouter(tags=['transactions'])


@router.get("/list_transactions", response_model=list[Transaction])
async def list_transaction(session: SessionDep):
    return session.exec(select(Transaction)).all()


@router.get("/read_transactions/{transaction_id}", response_model=Transaction)
async def read_transaction(transaction_id: int, session: SessionDep):
    transactions_db = session.get(Transaction, transaction_id)
    if not transactions_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaccion no existe"
        )
    return transactions_db


@router.post("/create_transactions", status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction_info: TransactionCreate, session: SessionDep):
    transaction_info_dict = transaction_info.model_dump()
    customer_db = session.get(Customer, transaction_info_dict.get('id_customer'))
    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaccion no existe"
        )
    transaction_db = Transaction.model_validate(transaction_info_dict)
    session.add(transaction_db)
    session.commit()
    session.refresh(transaction_db)
    return transaction_db


@router.delete("/delete_transactions/{transaction_id}")
async def delete_transaction(transaction_id: int, session: SessionDep):
    transactions_db = session.get(Transaction, transaction_id)
    if not transactions_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaccion no existe"
        )
    session.delete(transactions_db)
    session.commit()
    return {
        'customer_id': transaction_id,
        'detail': 'ok',
    }


@router.patch("/update_transactios/{transaction_id}", response_model=Transaction, status_code=status.HTTP_201_CREATED)
async def update_transaction(transaction_id: int, transaction_info: TransactionUpdate, session: SessionDep):
    transactions_db = session.get(Transaction, transaction_id)

    if not transactions_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaccion no existe"
        )
    transaction_info_dict = transaction_info.model_dump(exclude_unset=True)
    transactions_db.sqlmodel_update(transaction_info_dict)
    session.add(transactions_db)
    session.commit()
    session.refresh(transactions_db)
    return transactions_db
