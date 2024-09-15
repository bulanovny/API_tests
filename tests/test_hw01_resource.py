import httpx
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from core.hw01_contracts import SCHEME_RESOURCE_DATA

URL_BASE = "https://reqres.in"
URL_RESOURCE_LIST = "/api/unknown"
URL_RESOURCE_SINGLE = "/api/unknown/2"
URL_RESOURCE_NOT_FOUND = "/api/unknown/23"

def qa_resource_data(my_dict):
    validate(my_dict, SCHEME_RESOURCE_DATA)
    assert my_dict['color'].startswith("#")

def test_resource_not_found():
    response = httpx.get(URL_BASE + URL_RESOURCE_NOT_FOUND)
    assert response.status_code == 404

def test_resource_single():
    response = httpx.get(URL_BASE + URL_RESOURCE_SINGLE)
    assert response.status_code == 200
    qa_resource_data(response.json()['data'])

def test_resource_list():
    response = httpx.get(URL_BASE + URL_RESOURCE_LIST)
    assert response.status_code == 200
    for item in response.json()['data']:
        qa_resource_data(item)
