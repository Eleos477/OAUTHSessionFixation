import requests
from urllib import parse

# Unit testing for Oauth demo application. Only tests program functionality, does not actually demonstrate
#   session fixation vulnerabilities. For this, please see the step by step guides in the appropriate documentation.

def getResponseParams(response):
    parsed = parse.urlparse(response.url)
    params = parse.parse_qs(parsed.query)
    return params

def test_registration_page():
    ## Registration page returns ok
    response = requests.get("http://localhost:5000/register")
    assert response.status_code == 200

def test_login_page():
    ## Login page returns ok
    response = requests.get("http://localhost:5000/login")
    assert response.status_code == 200

def test_registration_process():
    session = requests.Session()
    
    ## Test registration is accepted
    response = session.post("http://localhost:5000/register", data={'fname':'test', 'lname':'test', 'password':'test'})
    assert "http://localhost:5000/register_complete" in response.url
    # Getting specified account number
    accountNum = int(getResponseParams(response)['accountNum'][0])

    ## Test can log in with just-created account
    response = session.post("http://localhost:5000/login", data={'accountNum': accountNum, 'password': 'test'})
    assert "Welcome test test!" in response.text # Verifying login page reached by checking page content

    ## Test can access banking page
    response = session.post("http://localhost:5000/banking")
    assert "Your balance:" in response.text

    return session, accountNum

def test_banking():
    # Get session from previous test
    session, accountNum = test_registration_process()
    
    ## Assert banking reached correctly
    response = session.post("http://localhost:5000/banking")
    assert "Your balance: $1000000" in response.text

    ## Assert can withdraw given amount (here $100)
    response = session.post("http://localhost:5000/banking", data={'amount': '100', 'withdraw': 'Withdraw'})
    response = session.get("http://localhost:5000/banking")
    assert "Your balance: $999900" in response.text

    ## Assert can deposit given amount (here $100)
    response = session.post("http://localhost:5000/banking", data={'amount': '100', 'deposit': 'Deposit'})
    response = session.get("http://localhost:5000/banking")
    assert "Your balance: $1000000" in response.text

    return session, accountNum

def test_logout():
    session, accountNum = test_banking()

    ## Assert logout returns to login page
    response = session.get("http://localhost:5000/logout")
    assert "Please login to continue" in response.text

    ## Assert can no longer access index page (redirects to login page)
    response = session.get("http://localhost:5000")
    assert "Please login to continue" in response.text

    ## Assert can no longer access banking page (redirects to login page)
    response = session.get("http://localhost:5000/banking")
    assert "Please login to continue" in response.text