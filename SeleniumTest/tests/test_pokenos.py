import requests

import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '4820d3fa9b872c438462ac46114fd094'

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id':2649})
    assert response.status_code == 200

def test_pert_of_body():
    respons = requests.put(f'{host}/trainers', headers={"trainer_token": token, "Content-Type":"application/json"},
                           json={
    "name": "RomanSavin888",
    "city": "Moscow"
})
    assert respons.json()["message"] == "Информация о тренере обновлена"

@pytest.mark.parametrize('key, value', [("trainer_name", "RomanSavin888"), 
                                        ("id", "2649"), 
                                        ("city", "Moscow")])
def test_response_json(key, value):
    response = requests.get(f'{host}/trainers', params={'trainer_id':2649})
    assert response.json()[key] == value