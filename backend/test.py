import json
import requests

data_request = {
    'id': '4',
    'name': 'supertest'
}

requests.post('http://127.0.0.1:8000/add-test/',
              data=json.dumps(data_request))
