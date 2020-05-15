from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        Homepage = HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        Homepage.getName().send_keys(getData["firstname"])
        Homepage.getEmail().send_keys(gteData["lastname"])
        Homepage.getCheck().click()
        self.selectoptionByText(Homepage.getGender(), getData["Gender"])
        Homepage.getSubmit().click()
        alertText = Homepage.getSuccessMessage().text
        assert ("success" in alertText)
        self.driver.refresh()
    @pytest.fixture(params=[{"firstname" : "Sonu", "lastname" : "Kumar", "gender" : "Male"}, {"firstname" : "Shreya", "lastname" : "Gupta", "gender" : "female"}])
    def getData(self, request):
        return request.param
