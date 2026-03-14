from src.app import activities


def test_signup_adds_participant(client):
    email = "new.student@mergington.edu"
    response = client.post("/activities/Chess%20Club/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for Chess Club"
    assert email in activities["Chess Club"]["participants"]


def test_signup_unknown_activity_returns_404(client):
    response = client.post(
        "/activities/Unknown%20Club/signup", params={"email": "student@mergington.edu"}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_duplicate_participant_returns_400(client):
    response = client.post(
        "/activities/Chess%20Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"


def test_signup_full_activity_returns_400(client):
    activity = activities["Chess Club"]
    activity["max_participants"] = len(activity["participants"])

    response = client.post(
        "/activities/Chess%20Club/signup",
        params={"email": "full.case@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Activity is full"


def test_signup_missing_email_returns_422(client):
    response = client.post("/activities/Chess%20Club/signup")

    assert response.status_code == 422
