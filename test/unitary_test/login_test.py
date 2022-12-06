from test.conftest import client

def test_should_status_code_ok(client):
	response = client.get('/')
	assert response.status_code == 200

def test_login(client):
    email = 'john@simplylift.co'
    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200

def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 302