import pytest
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait #explicit waits
from selenium.webdriver.support import expected_conditions as EC
#from locatortest import elem #untuk locator 
#from datatest import inputan #untuk inputan 


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
	
    def test_a_success_login(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") 
        driver.maximize_window() 

        linkText = driver.find_element(By.CLASS_NAME,'ico-login')
        linkText.click()
        driver.find_element(By.ID, 'Email').send_keys('dua22@gmail.com')
        driver.find_element(By.ID, 'Password').send_keys('duadua22') 
        linkCheck = driver.find_element(By.ID,'RememberMe')
        linkCheck.click()
        driver.find_element(By.CLASS_NAME, 'buttons').click()

        #implicit wait
        #driver.implicitly_wait(5)
        #self.assertEqual(driver.current_url, 'https://www.saucedemo.com/inventory.html')


    def test_b_fail_login(self): #no input pass
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") #untuk menyimpan url mana yang akan di test 
        driver.maximize_window() #untuk memaksimalkan tampilan window 

        linkText = driver.find_element(By.CLASS_NAME,'ico-login')
        linkText.click()
        driver.find_element(By.ID, 'Email').send_keys('dua22@gmail.com')
        driver.find_element(By.ID, 'Password').send_keys('') 
        linkCheck = driver.find_element(By.ID,'RememberMe')
        linkCheck.click()
        driver.find_element(By.CLASS_NAME, 'buttons').click()

        #respon = driver.find_element(By.CLASS_NAME, '[validation-summary-errors]').text
        #self.assertIn('Login was unsuccessful. Please correct the errors and try again.', respon)
        #driver.minimize_window()        



        
    

if __name__ == '__main__':
    unittest.main()