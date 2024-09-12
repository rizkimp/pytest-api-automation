import pytest
import requests
import json
from config.data import base_url

def test_list_of_all_objects():
    url = f"{base_url}"
    response = requests.get(url)
    json_response = response.json()
    assert response.status_code == 200
    assert json_response is not None
    assert len(json_response) == 13