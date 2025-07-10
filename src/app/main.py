import time
from fastapi import FastAPI, Response
from db_sqlite import create_all_tables
from app.routers import customers, invoices, transactions, plans


app = FastAPI(lifespan=create_all_tables)

@app.get("/")
async def root():
    return {"message": "root"}

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