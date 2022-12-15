import requests

#------------------------------------------------
def service(name, link_names):
    url = link_names[name]
    list_items = []
    items = requests.get(url=url)

    print(f"\n{name}: {items}")

    if(name == "keypairs"):
        names = [nm["name"] for nm in items.json()["keypairs"]]
        pb_keys = [i["public_key"] for i in items.json()["keypairs"]]

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

#------------------------------------------------
def get_names(name, link_names):
    list = service(name, link_names)
    image_names = [item["name"] for item in list]
    return(image_names)