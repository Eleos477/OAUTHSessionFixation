import requests

def test_oauthorization():
    url = 'http://127.0.0.1:8001/authorize'
    params = {'oauth_consumer_key': '9ebbd0b25760557393a43064a92bae539d962103'}
    resp = requests.post(url, data=params)

    assert resp.status_code == 500 # if try to authorize with invalid credentials and tokens then fail

def test_requesttokens():
    url = 'http://127.0.0.1:8001/initiate'
    params = {'oauth_consumer_key': '9ebbd0b25760557393a43064a92bae539d962103'}
    resp = requests.post(url, data=params)

    assert resp.status_code == 200 # check if tokens can be received

def test_requestuser():
    url = 'http://127.0.0.1:8001/user'
    params = {'token': '9ebbd0b25760557393a43064a92bae539d962103'}
    resp = requests.get(url, data=params)

    assert resp.status_code == 500 # using invalid token should fail when retrieving user detail


if __name__ == '__main__':
    test_oauthorization()
    test_requesttokens()
    test_requestuser()
