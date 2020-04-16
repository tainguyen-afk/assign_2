import unittest, csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class crm_test(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()



   def test_add_new_customers_with_csv_file(self):
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
       customers = []
       with open('customers.csv', 'r') as file:
           csv_reader = csv.reader(file, )
           for row in csv_reader:
               customers.append(row)

       for customer in customers:



           elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()


           elem = driver.find_element_by_id('id_cust_name')
           elem.send_keys(customer[0])
           elem = driver.find_element_by_id('id_organization')
           elem.send_keys(customer[1])

           elem = driver.find_element_by_id('id_role')
           elem.send_keys(customer[2])

           elem = driver.find_element_by_id('id_email')
           elem.send_keys(customer[3])

           elem = driver.find_element_by_id('id_bldgroom')
           elem.send_keys(customer[4])

           elem = driver.find_element_by_id('id_address')
           elem.send_keys(customer[5])
           elem = driver.find_element_by_id('id_account_number')
           elem.send_keys(customer[6])
           elem = driver.find_element_by_id('id_city')
           elem.send_keys(customer[7])
           elem = driver.find_element_by_id('id_state')
           elem.send_keys(customer[8])
           elem = driver.find_element_by_id('id_zipcode')
           elem.send_keys(customer[9])
           elem = driver.find_element_by_id('id_phone_number')
           elem.send_keys(customer[10])

           elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
           time.sleep(2)
           assert "customer added"

       driver.get("http://127.0.0.1:8000")
       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[2]/a").click()
       time.sleep(5)







   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()

