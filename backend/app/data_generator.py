import json
import pandas as pd
from faker import Faker

fake = Faker()

# Basic schema mapping (can be replaced with LLM schema inference)
def default_schema(domain: str):
    if domain == "healthcare":
        return ["name", "date_of_birth", "medical_condition"]
    elif domain == "finance":
        return ["name", "account_number", "balance"]
    else:
        return ["name", "email", "address"]

def generate_synthetic_data(prompt: str, num_rows: int, domain: str, fmt: str):
    schema = default_schema(domain)
    records = []
    for _ in range(num_rows):
        record = {}
        for field in schema:
            if field == "name":
                record[field] = fake.name()
            elif field == "date_of_birth":
                record[field] = str(fake.date_of_birth())
            elif field == "medical_condition":
                record[field] = fake.word()
            elif field == "email":
                record[field] = fake.email()
            elif field == "address":
                record[field] = fake.address()
            elif field == "account_number":
                record[field] = fake.iban()
            elif field == "balance":
                record[field] = round(fake.pyfloat(left_digits=5, right_digits=2), 2)
            else:
                record[field] = fake.word()
        records.append(record)
    
    df = pd.DataFrame(records)
    if fmt == "csv":
        return df.to_csv(index=False)
    return df.to_json(orient="records")
