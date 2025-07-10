from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.routers import customers, invoices, transactions, plans
from db_sqlite import create_all_tables


app = FastAPI(lifespan=create_all_tables)

security = HTTPBasic()

@app.get("/")
async def root(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if credentials.username == 'username' and credentials.password == 'password':
        return {"message": "Autorizado"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

app.include_router(customers.router)
app.include_router(invoices.router)
app.include_router(transactions.router)
app.include_router(plans.router)
