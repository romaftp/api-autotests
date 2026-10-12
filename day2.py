import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_json(path):
    response = requests.get(f"{BASE_URL}{path}", timeout=10)
    response.raise_for_status()
    return response.json()


users = get_json("/users")
print("Пользователей:", len(users))
for user in users:
    print(user["id"], user["name"], user["email"], user["address"]["city"])

posts = get_json("/posts")
posts_per_user = {}
for post in posts:
    user_id = post["userId"]
    posts_per_user[user_id] = posts_per_user.get(user_id, 0) + 1
print("Постов у каждого пользователя:", posts_per_user)

# Задача 1: пользователи с почтой на .biz
for user in users:
    if user["email"].endswith(".biz"):
        print("Пользователь с почтой на .biz:", user["name"], user["email"])

# Задача 2: функция, которая возвращает посты пользователя
def get_user_posts(user_id): 
    response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id}, timeout=10)
    return response.json()
print(len(get_user_posts(3)))

# Задача 3: пост с самым длинным заголовком
longest = posts[0]
for post in posts:
    if len(post["title"]) > len(longest["title"]):
        longest = post
print("Пост с самым длинным заголовком:", longest["id"], longest["title"])
print("Длина заголовка:", len(longest["title"]))