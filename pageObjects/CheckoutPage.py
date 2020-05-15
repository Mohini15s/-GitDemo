from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
    cardTitle = (By.XPATH, "//div[@class = 'card h-100']")
    #products = self.driver.find_elements_by_xpath("//div[@class = 'card h-100']")
    def getCardTiTle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)