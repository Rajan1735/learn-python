import requests
token = "bot6488739598:AAH_K5tJ1GgL9_6lKzZjhQaUdy8KQVVDNC0"
params = {
        "chat_id": "@hellorajan22",
        "text": "Good Morning"
    }

r = requests.post(
    f'https://api.telegram.org/{token}/sendMessage', params=params
)
print(r.json())
