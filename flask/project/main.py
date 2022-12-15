import requests
from flask import Flask, jsonify, request
from utils import service, instancing, validate
from settings import services, link_names

app = Flask(__name__)

# Images
@app.route('/images')
def getImages():
    list_images = service("images", link_names)
    return jsonify({"images": list_images})

# Networks
@app.route('/networks')
def getNetworks():
    list_networks = service("networks", link_names)
    return jsonify({"networks": list_networks})

# Flavors
@app.route('/flavors')
def getFlavors():
    list_flavors = service("flavors", link_names)
    return jsonify({"flavors": list_flavors})

# Keypairs
@app.route('/keypairs')
def getKeypairs():
    list_keypairs = service("keypairs", link_names)
    return jsonify({"keypairs": list_keypairs})

# Security Groups
@app.route('/security_groups')
def getGroups():
    list_groups = service("security_groups", link_names)
    return jsonify({"security_groups": list_groups})

# ---------------------------------------------
# Create instance
@app.route('/create', methods = ['POST'])
def createInstance():
    data = {
    "name" : request.json["name"],
    "image" : request.json["image"],
    "flavor" : request.json["flavor"],
    "networks" : request.json["networks"],
    "keypair" : request.json["keypair"],
    "security_group" : request.json["security_group"]
    }
    response = instancing(data)
    response.raise_for_status()
    return response.json()
    #return jsonify({"response" : response})

# ----------------------------------------------
if __name__ == '__main__':
    app.run(debug = True, port = 5000)