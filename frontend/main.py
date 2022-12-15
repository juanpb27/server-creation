import requests
from utils import service, get_names
from settings import link_names
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


# Images
@app.route('/home')
def showHome():
    image_names = get_names("images", link_names)
    networks_names = get_names("networks", link_names)
    flavor_names = get_names("flavors", link_names)
    keypairs_names = get_names("keypairs", link_names)
    sg_names = get_names("security_groups", link_names)

    return render_template(
        'index.html',
        images = image_names,
        networks = networks_names,
        flavors = flavor_names,
        keypairs = keypairs_names,
        sg = sg_names
        )


# ----------------------------------------------
if __name__ == '__main__':
    app.run(debug = True, port = 4000)