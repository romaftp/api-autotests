# 1. Словарь и вложенные поля
user = {"id": 1, "name": "romaftp", "address": {"city": "KZN"}, "email": "me@romaftp.ru"}
print(user["name"])
print(user["address"]["city"])

# 2. Список и цикл
posts = [{"id": 3, "title": "third"}, {"id": 2, "title": "second"}]
for post in posts:
    print(post["id"], post["title"])

# 3. Условие и проверка «есть ли ключ»
if "email" in user:
    print("email есть")
else:
    print("email нет")

# 4. f-строка
user_id = 5
print(f"https://jsonplaceholder.typicode.com/users/{user_id}")

# 5. Функция
def double(number):
    return number * 2

print(double(4))

# 6. Функция
def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet(name="romaftp", greeting="Привет")