import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_returns_200():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)
    assert response.status_code == 200


def test_get_post_has_required_fields():
    data = requests.get(f"{BASE_URL}/posts/1", timeout=10).json()
    for field in ("userId", "id", "title", "body"):
        assert field in data, f"В ответе нет поля {field}"


def test_get_post_id_matches_request():
    data = requests.get(f"{BASE_URL}/posts/1", timeout=10).json()
    assert data["id"] == 1


def test_get_posts_returns_100_items():
    response = requests.get(f"{BASE_URL}/posts", timeout=10)
    assert response.status_code == 200
    assert len(response.json()) == 100


def test_get_user_has_street_and_city():
    data = requests.get(f"{BASE_URL}/users/1", timeout=10).json()
    address = data["address"]
    assert "street" in address
    assert "city" in address


def test_get_post_comments_have_email():
    comments = requests.get(f"{BASE_URL}/posts/1/comments", timeout=10).json()
    assert isinstance(comments, list)
    for comment in comments:
        assert "email" in comment