import pytest
import requests
import json
from config.data import base_url

def test_add_object():
    payload = {
        "name": "MacBook Pro",
        "data": {
                "year": 2022,
                "price": 1000,
                "CPU model": "Intel Core i7",
                "Hard disk size": "512 MB"
            }
    }
    url = f"{base_url}"
    response_post = requests.post(url, json=payload)
    json_response_post = response_post.json()
    assert response_post.status_code == 200

    id_delete = json_response_post.get("id")
    assert id_delete is not None
    url_delete = f"{base_url}/{id_delete}"
    response_delete = requests.delete(url_delete)
    json_respose_delete = response_delete.json()
    x = f"Object with id = {id_delete} has been deleted."
    assert response_delete.status_code == 200
    assert json_respose_delete["message"] == x