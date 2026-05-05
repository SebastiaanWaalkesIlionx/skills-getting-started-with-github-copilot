import src.app as app_module


def test_unregister_removes_participant(client):
    email = "daniel@mergington.edu"

    response = client.delete(f"/activities/Chess%20Club/participants?email={email}")

    assert response.status_code == 200
    assert email not in app_module.activities["Chess Club"]["participants"]


def test_unregister_rejects_unknown_activity(client):
    response = client.delete("/activities/Unknown%20Club/participants?email=test@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_rejects_missing_participant(client):
    response = client.delete("/activities/Chess%20Club/participants?email=missing@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"
