import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert all('description' in v for v in data.values())

def test_signup_and_unregister():
    # Use a test email and activity
    test_email = "pytest@mergington.edu"
    activity_name = next(iter(client.get("/activities").json().keys()))

    # Sign up
    signup = client.post(f"/activities/{activity_name}/signup?email={test_email}")
    assert signup.status_code in (200, 400)  # 400 if already signed up

    # Unregister
    unregister = client.delete(f"/activities/{activity_name}/unregister?email={test_email}")
    assert unregister.status_code in (200, 400)  # 400 if not signed up
