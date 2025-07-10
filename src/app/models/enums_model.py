from enum import Enum


class StatusEnum(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class Examples(Enum):
    # customers
    CUSTOMER = {
        "name": "Jose",
        "description": "Cliente frecuente",
        "email": "jose@example.com",
        "age": 27
    }

    # invoice
    INVOICE = {
        "id_invoice": 0,
        "customer": {
            "name": "string",
            "description": "string",
            "email": "user@example.com",
            "age": 0,
            "id_customer": 0
        },
        "transactions": [
            {
            "amount": 0,
            "description": "string",
            "id_transaction": 0,
            "id_customer": 0
            }
        ],
        "total": 0
    }

    # transaction
    TRANSACTION = {
        "id_customer": 1,
        "amount": 100,
        "description": "Manzana",
    }

    # plan
    PLAN = {
        "name": "premium",
        "price": 1_000,
        "description": "Plan premium para usuario con posibilidades de ...",
    }

