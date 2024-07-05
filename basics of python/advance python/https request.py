import requests
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# print(r.text)
# print(r.status_code)

url = "https://api.github.com/user"
data = {
    "useranme": "user",
    "id": 'pass'
}
r2 = requests.post(url =url, data=data)
print(r2)