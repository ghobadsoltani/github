import requests
res= requests.get("https://www.tgju.org/profile/geram18")
print(res.status_code)
print(res.text)