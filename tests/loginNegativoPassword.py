import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginNegativeScenarios:
    @pytest.mark.login_negativo_pass
    def test_negative_password(self):

        #Iniciar el navegador Firefox
        driver = webdriver.Firefox()

        #Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        #Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        #Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("incorrectPassword")

        #Push Submit button
        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()

        #Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed"

        #Verify error message text is Your password is invalid!
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message is not expected"

