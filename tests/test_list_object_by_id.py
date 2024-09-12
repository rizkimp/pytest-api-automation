import pytest
import requests
import json
from config.data import base_url

def test_list_object_by_id():
    url = f"{base_url}?id=3"
    response = requests.get(url)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response[0]["id"] == "3"
    assert json_response[0]["name"] == "Apple iPhone 12 Pro Max"
    assert json_response[0]["data"]["color"] == "Cloudy White"
    assert json_response[0]["data"]["capacity GB"] == 512