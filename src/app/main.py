import time
from typing import Annotated
from db_sqlite import create_all_tables
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.routers import customers, invoices, transactions, plans
from fastapi import FastAPI, Response, Depends, HTTPException, status


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


@app.middleware('http')
async def log_request_time(request: Response, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"[LOG - INFO] -> Request: [{request.url}] completed in [{process_time:4f}] seconds")
    return response