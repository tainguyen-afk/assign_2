import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class crm_test(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_customer_CRUD(self):
       user = "instructor"
       pwd = "maverick1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)

       assert "Logged In"
       time.sleep(5)

       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/th/a").click()

       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()

       elem = driver.find_element_by_id('id_cust_name')
       elem.send_keys('Barbara York')
       elem = driver.find_element_by_id('id_organization')
       elem.send_keys('This is a selenium test')

       elem = driver.find_element_by_id('id_role')
       elem.send_keys('This is a selenium test')

       elem = driver.find_element_by_id('id_email')
       elem.send_keys('selenium@gmail.com')

       elem = driver.find_element_by_id('id_bldgroom')
       elem.send_keys('123')

       elem = driver.find_element_by_id('id_address')
       elem.send_keys('This is a selenium test')
       elem = driver.find_element_by_id('id_account_number')
       elem.send_keys('456')
       elem = driver.find_element_by_id('id_city')
       elem.send_keys('This is a selenium test')
       elem = driver.find_element_by_id('id_state')
       elem.send_keys('NE')
       elem = driver.find_element_by_id('id_zipcode')
       elem.send_keys('67896')
       elem = driver.find_element_by_id('id_phone_number')
       elem.send_keys('123456789')
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()

       assert "customer added"



       driver.get("http://127.0.0.1:8000")
       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()


       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[12]/a").click()
       time.sleep(5)


       driver.find_element_by_id('id_organization').clear()
       driver.find_element_by_id('id_role').clear()
       driver.find_element_by_id('id_bldgroom').clear()
       driver.find_element_by_id('id_email').clear()
       driver.find_element_by_id('id_account_number').clear()
       driver.find_element_by_id('id_city').clear()
       driver.find_element_by_id('id_address').clear()
       driver.find_element_by_id('id_state').clear()
       driver.find_element_by_id('id_zipcode').clear()
       driver.find_element_by_id('id_phone_number').clear()
       time.sleep(5)

       elem = driver.find_element_by_id('id_cust_name')
       for option in elem.find_elements_by_tag_name('option'):
           if option.text == 'Barbara York':
               option.click()

       elem = driver.find_element_by_id('id_organization')
       elem.send_keys('This is an update')

       elem = driver.find_element_by_id('id_role')
       elem.send_keys('This is an update')

       elem = driver.find_element_by_id('id_email')
       elem.send_keys('selenium@gmail.com')

       elem = driver.find_element_by_id('id_bldgroom')
       elem.send_keys('789')

       elem = driver.find_element_by_id('id_address')
       elem.send_keys('This is an update')
       elem = driver.find_element_by_id('id_account_number')
       elem.send_keys('789')
       elem = driver.find_element_by_id('id_city')
       elem.send_keys('This is an update')
       elem = driver.find_element_by_id('id_state')
       elem.send_keys('NE')
       elem = driver.find_element_by_id('id_zipcode')
       elem.send_keys('67896')
       elem = driver.find_element_by_id('id_phone_number')
       elem.send_keys('123456789')





       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
       time.sleep(5)

       assert "customer updated"
       driver.get("http://127.0.0.1:8000")
       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()

       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[14]/a").click()
       time.sleep(5)
       assert "view customer summary"

       driver.get("http://127.0.0.1:8000")
       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()
       time.sleep(5)



       elem = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[13]/a').click()
       time.sleep(5)
       ale = driver.switch_to.alert
       ale.accept()
       time.sleep(5)
       assert "customer deleted"
       driver.get("http://127.0.0.1:8000")
       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()
       time.sleep(5)





   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()

