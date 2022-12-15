#!/usr/bin/python3
"""
index api
"""
from flask import jsonify, Flask
from api.v1.views import app_views
from models import storage
app = Flask(__name__)


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """return tuple"""

    return jsonify(status='OK')


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def counter():
    """counter for obj"""

    table = {
        "amenities": storage.count('Amenity'),
        "cities": storage.count('City'),
        "places": storage.count('Place'),
        "reviews": storage.count('Review'),
        "states": storage.count('State'),
        "users": storage.count('User')
    }

    """
    status_code = 200
   and content_type = "application/json"
    """
    count = jsonify(table)
    return count
