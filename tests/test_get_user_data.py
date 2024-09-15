import httpx
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from core.contracts import USER_DATA_SCHEME

BASE_URL = "https://reqres.in"
LIST_USERS = "/api/users?page=2"
SINGLE_USER = "/api/users/2"
ENDS_WITH = "@reqres.in"

def test_list_users():
    response = httpx.get(BASE_URL + LIST_USERS)
    assert response.status_code == 200
    # print(response.text)
    data = response.json()['data']

    print('\n')

    for element in data:
        # print(element)
        try:
            validate(element, USER_DATA_SCHEME)
        except ValidationError as e:
            print('We have an exception while validation: ')
            print(e.args)

        assert element['email'].endswith(ENDS_WITH)
        link = 'https://reqres.in/img/faces/' + str(element['id']) + '-image.jpg'
        assert element['avatar'] == link


def test_single_user():
    response = httpx.get(BASE_URL + SINGLE_USER)
    assert response.status_code == 200
    data = response.json()['data']

    validate(data, USER_DATA_SCHEME)
    assert data['email'].endswith(ENDS_WITH)
    link = 'https://reqres.in/img/faces/' + str(data['id']) + '-image.jpg'
    assert data['avatar'] == link





