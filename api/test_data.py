import uuid
import random


def generate_user_data():

    return {
        "name": "TestName",
        "email": f"Test{uuid.uuid4().hex[:6]}@example.com",
        "password": "Test123!",
        "title": random.choice(["Mr", "Mrs", "Miss"]),
        "birth_date": "21",
        "birth_month": "10",
        "birth_year": "1998",
        "firstname": "FirstTestName",
        "lastname": "LastTestName",
        "company": "TestCompany",
        "address1": "TestAddress1",
        "address2": "TestAddress2",
        "country": "USA",
        "zipcode": "10001",
        "state": "TestState",
        "city": "TestCity",
        "mobile_number": "5551234567",
    }
