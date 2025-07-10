from sqlmodel import select
from db_sqlite import SessionDep
from fastapi import APIRouter, status, HTTPException
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


@router.get("/read_transactions/{id_transaction}", response_model=Transaction)
async def read_transaction(id_transaction: int, session: SessionDep):
    transactions_db: Transaction = session.get(Transaction, id_transaction)
    if not transactions_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaccion no existe"
        )
    return transactions_db


@router.post("/create_transactions", status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction_info: TransactionCreate, session: SessionDep):
    transaction_info_dict = transaction_info.model_dump()
    customer_db: Customer = session.get(Customer, transaction_info_dict.get('id_customer'))
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


@router.delete("/delete_transactions/{id_transaction}")
async def delete_transaction(id_transaction: int, session: SessionDep):
    transactions_db: Transaction = session.get(Transaction, id_transaction)
    if not transactions_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaccion no existe"
        )
    session.delete(transactions_db)
    session.commit()
    return {
        'id_customer': id_transaction,
        'detail': 'ok',
    }


@router.patch("/update_transactios/{id_transaction}", response_model=Transaction, status_code=status.HTTP_201_CREATED)
async def update_transaction(id_transaction: int, transaction_info: TransactionUpdate, session: SessionDep):
    transactions_db: Transaction = session.get(Transaction, id_transaction)

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
