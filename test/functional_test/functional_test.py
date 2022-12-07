import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


home_page_url = 'http://127.0.0.1:5000/'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


class TestFunctional:
    def test_functional(self):
        driver.get(home_page_url)
        form_input = driver.find_element(By.NAME, "email")
        form_input.send_keys("john@simplylift.co")
        time.sleep(1.5)
        form_button = driver.find_element(By.ID, "button")
        form_button.submit()
        assert "Summary | GUDLFT Registration" in driver.title
        time.sleep(1.5)
        booking_button = driver.find_element(By.ID, "bookingbutton")
        booking_button.click()
        time.sleep(1.5)
        """On Book enter the number of places"""
        purchase_input = driver.find_element(By.ID, "spots")
        purchase_input.clear()
        purchase_input.send_keys(1)
        time.sleep(1.5)
        purchase_button = driver.find_element(By.ID, "submitbutton")
        purchase_button.click()
        """Gives the confirmation page"""
        time.sleep(1.5)
        assert "Great-booking complete!" in driver.find_element(By.ID, "message").text
        driver.quit()