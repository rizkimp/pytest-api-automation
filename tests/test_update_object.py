import pytest
import requests
import json
from config.data import base_url

def test_update_object():
    id = "ff80818191b5c4090191b6ba08da02f4"
    payload = {
                "name": "Apple MacBook Pro 16",
                    "data": {
                        "year": 2019,
                        "price": 2049.99,
                        "CPU model": "Intel Core i9",
                        "Hard disk size": "512 GB",
                        "color": "silver"
                    }
            }
    url = f"{base_url}/{id}"
    response = requests.put(url, json=payload)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response["id"] == id
    assert json_response["name"] == payload["name"]
    assert json_response["updatedAt"] != ""
    assert json_response["data"]["year"] == payload["data"]["year"]
    assert json_response["data"]["price"] == payload["data"]["price"]
    assert json_response["data"]["CPU model"] == payload["data"]["CPU model"]
    assert json_response["data"]["Hard disk size"] == payload["data"]["Hard disk size"]
    assert json_response["data"]["color"] == payload["data"]["color"]
    