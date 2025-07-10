from fastapi import FastAPI
from app.routers import customers, invoices, transactions, plans
from db_sqlite import create_all_tables


app = FastAPI(lifespan=create_all_tables)

@app.get("/")
async def root():
    return {"message": "root"}

app.include_router(customers.router)
app.include_router(invoices.router)
app.include_router(transactions.router)
app.include_router(plans.router)
