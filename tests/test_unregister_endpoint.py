from src.app import activities


def test_unregister_removes_participant(client):
    email = "michael@mergington.edu"
    response = client.delete("/activities/Chess%20Club/participants", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from Chess Club"
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    response = client.delete(
        "/activities/Unknown%20Club/participants", params={"email": "student@mergington.edu"}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_missing_participant_returns_404(client):
    response = client.delete(
        "/activities/Chess%20Club/participants",
        params={"email": "not.registered@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"


def test_unregister_missing_email_returns_422(client):
    response = client.delete("/activities/Chess%20Club/participants")

    assert response.status_code == 422
