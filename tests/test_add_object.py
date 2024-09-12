import pytest
import requests
import json
from config.data import base_url

def test_add_object():
    payload = {
        "name": "MacBook Pro",
        "data": {
                "year": 2022,
                "price": 1800,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
    }
    url = f"{base_url}"
    response = requests.post(url, json=payload)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response["id"] != ""
    assert json_response["name"] == payload["name"]
    assert json_response["data"]["year"] == payload["data"]["year"]
    assert json_response["data"]["price"] == payload["data"]["price"]
    assert json_response["data"]["Hard disk size"] == payload["data"]["Hard disk size"]