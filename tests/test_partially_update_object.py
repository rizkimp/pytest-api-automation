import pytest
import requests
import json
from config.data import base_url

def test_partially_update_object():
    id = "ff80818191bc65680191bd224749020d"
    payload = {
                "name": "Apple MacBook Pro 13 (Updated Name)"
            }
    url = f"{base_url}/{id}"
    response = requests.patch(url, json=payload)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response["id"] == id
    assert json_response["name"] ==  payload["name"]