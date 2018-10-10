from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import allure
from allure_commons.types import AttachmentType
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self, test_setup):
        try:
            driver = self.driver
            driver.get(utils.URL)
            login = LoginPage(driver)
            login.enter_username(utils.USERNAME)
            login.enter_password(utils.PASSWORD)
            login.click_login()
        except:
            print("Some exception occurred")
            raise

    def test_logout(self,test_setup):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            print(x)
            assert x == "OrangeHRM"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%H-%M-%S_%m-%d-%Y")
            testName = utils.whoami()
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            utils.save_screenshot(driver, screenshotName)
            raise
        except:
            print("Some exception occurred")
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot_",
                          attachment_type=allure.attachment_type.PNG)
            raise

        else:
            print("No exceptions occurred")
        finally:
            print("This block will always execute | Close DB")


