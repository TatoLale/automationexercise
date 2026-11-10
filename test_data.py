import uuid
import random


def generate_user_data():

    return {
        "name": "TestName",
        "email": f"Test{uuid.uuid4().hex[:6]}@example.com",
        "password": "Test123!",
        "title": random.choice(["Mr", "Mrs"]),
        "birth_date": "10",
        "birth_month": "August",
        "birth_year": "1967",
        "firstname": "FirstTestName",
        "lastname": "LastTestName",
        "company": "TestCompany",
        "address1": "TestAddress1",
        "address2": "TestAddress2",
        "country": "United States",
        "zipcode": "10001",
        "state": "TestState",
        "city": "TestCity",
        "mobile_number": "5551234567",
    }
