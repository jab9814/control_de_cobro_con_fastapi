from fastapi import APIRouter
from app.models.invoice_model import Invoice


router = APIRouter(tags=['invoices'])

@router.post("/invoices")
async def create_invoice(invoices_info: Invoice):
    return invoices_info

