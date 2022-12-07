import pytest
from test.conftest import client



def test_reservation(client):
    email = 'john@simplylift.co'
    club = "Simply Lift"
    competition = "Small Challenge"
    placesRequired = 1

    user_session = client.post('/showSummary', data={'email': email})
    booking_response = client.get('/book/Spring%20Festival/Simply%20Lift', data={"foundClub": club, "foundCompetition": competition})
    purchase_response = client.post('/purchasePlaces', data={"club": club, "competition": competition, "places": placesRequired})
    data = purchase_response.data.decode()

    assert purchase_response.status_code == 200
    assert "Great-booking complete!" in data