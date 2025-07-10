from pydantic import BaseModel
from app.models.enums_model import Examples
from app.models.customer_model import Customer
from app.models.transaction_model import Transaction


class Invoice(BaseModel):
    id_invoice: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property
    def amount_total(self):
        return sum(transaction.amount for transaction in self.transactions)
    
    model_config = {
        "json_schema_extra": {
            "examples": [Examples.INVOICE.value]
        }
    }