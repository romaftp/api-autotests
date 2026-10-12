import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/9999", timeout=10)
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print("Сервер ответил ошибкой:", error)
except requests.exceptions.RequestException as error:
    print("Запрос не удался:", error)