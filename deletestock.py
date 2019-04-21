import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class Deletestock(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-user-media-security=true")
        self.driver = webdriver.Chrome("C:/Users/Jayanth/PycharmProjects/test/venv/chromedriver.exe")

    def test_deletestock(self):

        driver = self.driver
        #to  maximze the chrome

        driver.maximize_window()
        driver.get("https://eaglefinancialservicesefs.herokuapp.com/")
        elem = driver.find_element_by_xpath("// *[ @ id =\"myNavbar\"] / ul[2] / li / a / span")
        elem.click()
        time.sleep(1)

        #logging in as a user
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("instructor")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("instructor1a")
        elem = driver.find_element_by_xpath("// *[ @ id = \"app-layout\"] / div / div / div / div / form / p[3] / input")
        elem.click()
        time.sleep(5)

        assert "logged in"


        #Deleting stock

        elem =driver.find_element_by_xpath("// *[ @ id = \"app-layout\"] / div / div / div / div[2] / div / "
                                           "div / div / div / div[3] / div / div / p[2] / a")
        elem.click()
        time.sleep(1)

        elem = driver.find_element_by_xpath("// *[ @ id = \"app-layout\"] / div / div / div / "
                                            "div[3] / table / tbody / tr / td[8] / a" )

        elem.click()

        obj = driver.switch_to.alert
        obj.accept()
        driver.refresh()
        time.sleep(5)



    def teardown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()


