import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class Add_Customer(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-user-media-security=true")
        self.driver = webdriver.Chrome("C:/Users/Jayanth/PycharmProjects/test/venv/chromedriver.exe")

    def test_addcustomer(self):

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

        #Adding new customer

        elem =driver.find_element_by_xpath("// *[ @ id = \"app-layout\"] / div / div / div / div[2] /"
                                           " div / div / div / div / div[1] / div / div / p[2] / a")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath(" // *[ @ id = \"app-layout\"] / div / div / div / div[3] / div / a / span")
        elem.click()
        elem = driver.find_element_by_id("id_cust_number")
        elem.send_keys("12345")
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Jayanth")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("7535 Pierce plaza")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_id("id_state")
        elem.send_keys("Nebraska")
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("68124")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("jayanth@gmail.com")
        elem = driver.find_element_by_id("id_cell_phone")
        elem.send_keys("5713534021")
        time.sleep(5)
        elem = driver.find_element_by_xpath("// *[ @ id = \"app-layout\"] / div / div / div / form / button")
        elem.click()
        time.sleep(2)





    def teardown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()


