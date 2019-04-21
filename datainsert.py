import dataread
from selenium import webdriver
import time


driver = webdriver.Chrome("C:/Users/Jayanth/PycharmProjects/test/venv/chromedriver.exe")

driver.maximize_window()

driver.get("https://eaglefinancialservicesefs.herokuapp.com/")

elem = driver.find_element_by_xpath("// *[ @ id =\"myNavbar\"] / ul[2] / li / a / span")
elem.click()
time.sleep(1)

# logging in as a user
elem = driver.find_element_by_id("id_username")
elem.send_keys("instructor")
elem = driver.find_element_by_id("id_password")
elem.send_keys("instructor1a")
elem = driver.find_element_by_xpath("// *[ @ id = \"app-layout\"] / div / div / div / div / form / p[3] / input")
elem.click()
time.sleep(5)

assert "logged in"

# Adding new customer

elem = driver.find_element_by_xpath("// *[ @ id = \"app-layout\"] / div / div / div / div[2] /"
                                    " div / div / div / div / div[1] / div / div / p[2] / a")
elem.click()
time.sleep(1)
elem = driver.find_element_by_xpath(" // *[ @ id = \"app-layout\"] / div / div / div / div[3] / div / a / span")
elem.click()

path= "C:/Users/Jayanth/Desktop/Sample Eagle Financial Services Data.xlsx"

rows = dataread.getrowcount(path, 'sheet1')

for r in range(3,rows+1):
    cust_number=dataread.readdata(path,"sheet1",r,1)
    name = dataread.readdata(path,"sheet1", r, 2)
    email = dataread.readdata(path,"sheet1", r, 3)
    address = dataread.readdata(path,"sheet1", r, 4)
    city= dataread.readdata(path,"sheet1", r, 5)
    state=dataread.readdata(path,"sheet1", r, 6)
    zip=dataread.readdata(path,"sheet1", r, 7)
    cell_phone=dataread.readdata(path,"sheet1", r, 8)

    elem = driver.find_element_by_id("id_cust_number")
    elem.send_keys(cust_number)
    elem = driver.find_element_by_id("id_name")
    elem.send_keys(name)
    elem = driver.find_element_by_id("id_address")
    elem.send_keys(address)
    elem = driver.find_element_by_id("id_city")
    elem.send_keys(city)
    elem = driver.find_element_by_id("id_state")
    elem.send_keys("Nebraska")
    elem = driver.find_element_by_id("id_zipcode")
    elem.send_keys(zip)
    elem = driver.find_element_by_id("id_email")
    elem.send_keys(email)
    elem = driver.find_element_by_id("id_cell_phone")
    elem.send_keys(cell_phone)
    time.sleep(5)
    elem = driver.find_element_by_xpath("// *[ @ id = \"app-layout\"] / div / div / div / form / button")
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_xpath(" // *[ @ id = \"app-layout\"] / div / div / div / div[3] / div / a / span")
    elem.click()





    def teardown(self):
        self.driver.close()
