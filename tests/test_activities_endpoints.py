def test_get_activities_returns_dictionary(client):
    response = client.get("/activities")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_get_activities_items_have_expected_structure(client):
    response = client.get("/activities")
    data = response.json()

    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)
