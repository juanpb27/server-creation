# --------------Utils------------------
# External Functions
import requests
from flask import request
from settings import url_env, payload, services, link_names

# My Functions
# --------------------------------------------
def start():
    url_auth = link_names["token"]
    token = requests.post(url=url_auth, json=payload)
    auth_id = token.json()['token']['id']

    headers={"X-Auth-Token":auth_id}
    return headers

# --------------------------------------------
def service(name, link_names):
    url = link_names[name]
    list_items = []
    items = requests.get(url=url, headers=start())
    print(f"\n{name}: {items}")

    if(name == "keypairs"):
        names = [nm["keypair"]["name"] for nm in items.json()[name]]
        pb_keys = [i["keypair"]["public_key"] for i in items.json()[name]]

        for i in range(len(names)):
            list_items.append({
            "name": names[i],
            "public_key" : pb_keys[i]
            })

    else:
        names = [nm["name"] for nm in items.json()[name]]
        ids = [i["id"] for i in items.json()[name]]

        for i in range(len(names)):
            list_items.append({
            "name": names[i],
            "id" : ids[i]
            })

    return list_items

#---------------------------------------------
def instancing(data):
    url = link_names["instance"]
    specifications = {
        "server" : {
            "name" : data["name"],
            "imageRef" : data["image"],
            "flavorRef" : data["flavor"],
            "networks" : data["networks"],
            "key_name" : data["keypair"],
            "security_groups" : [{"name" : data["security_group"]}]
        }
    }
    response = requests.post(url=url, headers=start(), json=specifications)
    print(response.json())
    print(specifications)
    return response

# --------------------------------------------
def validate(wanted, source):
    metadata = {}
    flag = 0

    for item in source:
        if wanted == item["name"]:
            metadata["name"] = item["name"]
            metadata["id"] = item["id"]
            print(metadata)
            flag = 1

    if flag == 0:
        print("Incorrect image name. Try again")