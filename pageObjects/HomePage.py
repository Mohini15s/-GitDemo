from selenium.webdriver.common.by import By
class HomePage:
    def __init__(self, driver):
        self.driver = driver
    shop = (By.CSS_SELECTOR, "[name='name']")
    name = (By.CSS_SELECTOR, "a[href *= 'shop']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.CSS_SELECTOR, "[class = 'alert-success']")


    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheck(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

