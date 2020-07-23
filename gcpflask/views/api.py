from flask import request, url_for, jsonify
from flask_restful import Resource, abort


import csv

from ..server import app, api

## Obtain Data -----------------------------------------------------------------
# This is an example of reading from file. You could also serve files for
# download, or models that the application serves.

# Name, Hex, RGB with lookup by name in lowercase
with open("gcpflask/static/data/crayons.csv") as fd:
    csv_reader = csv.reader(fd, delimiter=",")
    crayons = {row[0].lower().replace(" ", "-"): row for row in csv_reader}


## API Helpers -----------------------------------------------------------------


def abort_if_crayon_doesnt_exist(name):
    if name.lower() not in crayons:
        abort(404, message="Crayon {} does not exist".format(name))


## API Views -------------------------------------------------------------------
# These urls demonstrate how to serve a RESTful API
# See https://flask-restful.readthedocs.io/en/latest/quickstart.html


class APIIndex(Resource):
    """The API index exposes all endpoints for the user
    """

    def get(self):
        views = {
            "/api/": request.host_url.rstrip("/") + url_for("api_index"),
            "/api/crayons/": request.host_url.rstrip("/") + url_for("crayons"),
            "/api/crayons/<string:name>/": request.host_url.rstrip("/")
            + url_for("api_index")
            + "<string:name>",
        }
        return jsonify(views)


def single_crayon(name):
    """This view serves a single representation of a crayon, and is shared between
       the crayons list and crayon get functions.
    """
    crayon = crayons.get(name)
    return {
        "url": request.host_url.rstrip("/") + url_for("crayon_detail", name=name),
        "name": crayon[0],
        "hex": crayon[1],
        "rgb": crayon[2],
    }


class SingleCrayon(Resource):
    """Get a single crayon. Note that you can add a put/post here to create
       a new crayon, and the same goes for ListCrayons
    """

    def get(self, name):
        abort_if_crayon_doesnt_exist(name)
        name = name.lower()
        return single_crayon(name)


class ListCrayons(Resource):
    """Return a list of crayons
    """

    def get(self):
        return jsonify([single_crayon(name) for name in sorted(crayons.keys())])


api.add_resource(APIIndex, "/api/", endpoint="api_index")
api.add_resource(ListCrayons, "/api/crayons/", endpoint="crayons")
api.add_resource(SingleCrayon, "/api/crayons/<string:name>/", endpoint="crayon_detail")
