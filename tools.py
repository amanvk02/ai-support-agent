import json 
from pathlib import Path 

DATA_DIR = Path(__file__).resolve().parent / "data"

def get_customer_settings(customer_id: str) -> dict:
    customers = json.loads(
        (DATA_DIR / "customers.json").read_text()
    )

    customer = customers.get(customer_id)

    if customer is None: 
        return {"error": "Customer not found"}

    return {
        "evidence_id": f"settings:{customer_id}",
        "customer_id": customer_id,
        **customer
    }