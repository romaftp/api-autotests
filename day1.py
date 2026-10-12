import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.get(f"{BASE_URL}/posts/1", timeout=10)

print("Статус:", response.status_code)
print("Content-Type:", response.headers["Content-Type"])
print("Время ответа, с:", response.elapsed.total_seconds())
print("Тело:", response.json())