from fastapi.testclient import TestClient
from fastapi import status, HTTPException

from location import app, Location, get_location_or_404


locations = {
    "zeeshan": Location(name="Zeeshan", location="Karachi"),
    "javed": Location(name="Javed", location="Lahore"),
}

def fake_get_location_or_404(name:str)->Location:
    loc = locations.get(name.lower())
    if not loc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No location found for {name}")
    return loc

# Comment out this line to stop overriding the dependency
app.dependency_overrides[get_location_or_404] = fake_get_location_or_404

client = TestClient(app)


def test_read_location():
    response = client.get("/location/zeeshan")
    assert response.status_code == 200
    assert response.json() == {"name": "Zeeshan", "location": "Karachi"}

def test_location_404():
    response = client.get("/location/john")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    