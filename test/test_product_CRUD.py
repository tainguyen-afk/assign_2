import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class crm_test(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_product_CRUD(self):
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
       driver.get("http://127.0.0.1:8000")
       assert "Logged In"
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[4]/a").click()
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a").click()
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/div/select").click()


       elem = driver.find_element_by_id('id_cust_name')
       for option in elem.find_elements_by_tag_name('option'):
           if option.text == 'Barbara York':
               option.click()
       elem = driver.find_element_by_id('id_product')
       elem.send_keys("This is a test post with selenium")


       elem = driver.find_element_by_id('id_p_description')
       elem.send_keys("This is a test post with selenium")


       elem = driver.find_element_by_id('id_quantity')
       elem.send_keys("300")


       elem = driver.find_element_by_id('id_charge')
       elem.send_keys("1000")
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
       time.sleep(5)

       assert "product created"
       driver.get("http://127.0.0.1:8000")
       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[4]/a").click()
       time.sleep(5)

       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr/td[7]/a").click()
       time.sleep(5)


       driver.find_element_by_id('id_product').clear()
       driver.find_element_by_id('id_p_description').clear()
       driver.find_element_by_id('id_quantity').clear()
       driver.find_element_by_id('id_charge').clear()
       time.sleep(5)

       elem = driver.find_element_by_id('id_cust_name')
       for option in elem.find_elements_by_tag_name('option'):
           if option.text == 'Barbara York':
               option.click()

       elem = driver.find_element_by_id('id_product')
       elem.send_keys("This is an update")


       elem = driver.find_element_by_id('id_p_description')
       elem.send_keys("This is an update")


       elem = driver.find_element_by_id('id_quantity')
       elem.send_keys("456")


       elem = driver.find_element_by_id('id_charge')
       elem.send_keys("123")
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
       time.sleep(5)

       assert "service updated"
       driver.get("http://127.0.0.1:8000")
       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[4]/a").click()
       time.sleep(5)

       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr/td[8]/a").click()
       time.sleep(5)
       ale = driver.switch_to.alert
       ale.accept()
       time.sleep(5)
       assert "service deleted"

       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[4]/a").click()
       time.sleep(5)





   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()

