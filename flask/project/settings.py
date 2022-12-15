url_env = 'https://api-uat-001.ormuco.com'

payload = {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "workshop2022@utb.edu.co",
                    "domain": {
                        "name": "Default"
                    },
                    "password": "ILOVECLOUD2022"
                }
            }
        }
    }
}

services = {
    "token": {
        "port" : ":5000",
        "ep" : "/v3/auth/tokens"
    },

    "images": {
        "port" : ":9292",
        "ep" : "/v2/images"
    },

    "networks": {
        "port" : ":9696",
        "ep" : "/v2.0/networks"
    },

    "flavors": {
        "port" : ":8774",
        "ep" : "/v2.1/flavors"
    },

    "keypairs": {
        "port" : ":8774",
        "ep" : "/v2.1/os-keypairs"
    },

    "security_groups": {
        "port" : ":9696",
        "ep" : "/v2.0/security-groups"
    },

    "instance" : {
        "port" : ":8774",
        "ep" : "/v2.1/servers"
    }
}

link_names = {
    "token" : url_env + services["token"]["port"] + services["token"]["ep"],
    "images" :url_env + services["images"]["port"] + services["images"]["ep"],
    "networks": url_env + services["networks"]["port"] + services["networks"]["ep"],
    "flavors":url_env + services["flavors"]["port"] + services["flavors"]["ep"],
    "keypairs": url_env + services["keypairs"]["port"] + services["keypairs"]["ep"],
    "security_groups" : url_env + services["security_groups"]["port"] + services["security_groups"]["ep"],
    "instance" : url_env + services["instance"]["port"] + services["instance"]["ep"]
}