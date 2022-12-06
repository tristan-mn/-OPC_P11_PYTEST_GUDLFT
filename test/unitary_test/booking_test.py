from test.conftest import client
from flask import request, flash
import pytest

@pytest.mark.usefixtures("client")
class TestBook():
    def test_book_successful(self, client):
        club = "Simply Lift"
        competition = "Spring Festival"
        response = client.get('/book/Spring%20Festival/Simply%20Lift', data={"foundClub": club, "foundCompetition": competition})
        assert response.status_code == 200


@pytest.mark.usefixtures("client")
class TestPurchase():
    def test_purchases_successful(self, client):
        club = "Simply Lift"
        competition = "Spring Festival"
        placesRequired = "5"
        response = client.post('/purchasePlaces', data={"club": club, "competition": competition, "places": placesRequired})
        data = response.data.decode()
        assert response.status_code == 200
        assert "Great-booking complete!" in data

    def test_purchase_not_enough_points(self, client):
        club = "Iron Temple"
        competition = "Spring Festival"
        placesRequired = "12"
        response = client.post('/purchasePlaces', data={"club": club, "competition": competition, "places": placesRequired})
        assert response.status_code == 200
        assert "enough points" in response.data.decode()