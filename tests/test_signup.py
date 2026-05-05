import src.app as app_module


def test_signup_adds_new_participant(client):
    email = "new.student@mergington.edu"

    response = client.post(f"/activities/Chess%20Club/signup?email={email}")

    assert response.status_code == 200
    assert email in app_module.activities["Chess Club"]["participants"]


def test_signup_rejects_duplicate_participant(client):
    email = "michael@mergington.edu"

    response = client.post(f"/activities/Chess%20Club/signup?email={email}")

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_rejects_unknown_activity(client):
    response = client.post("/activities/Unknown%20Club/signup?email=test@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_rejects_when_activity_is_full(client):
    app_module.activities["Soccer Team"]["participants"] = [
        f"student{i}@mergington.edu" for i in range(app_module.activities["Soccer Team"]["max_participants"])
    ]

    response = client.post("/activities/Soccer%20Team/signup?email=overflow@mergington.edu")

    assert response.status_code == 400
    assert response.json()["detail"] == "Activity is full"
