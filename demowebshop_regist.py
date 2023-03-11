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


class TestRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
	
    def test_a_success_regist(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") 
        driver.maximize_window() #untuk memaksimalkan tampilan window 

        linkText = driver.find_element(By.CLASS_NAME,'ico-register')
        linkText.click()
        driver.find_element(By.ID, 'FirstName').send_keys('dua') #inspek elemen by ID
        driver.find_element(By.ID, 'LastName').send_keys('dua') 
        driver.find_element(By.ID, 'Email').send_keys('dua22@gmail.com')
        driver.find_element(By.ID, 'Password').send_keys('duadua22')
        driver.find_element(By.ID, 'ConfirmPassword').send_keys('duadua22') 
        driver.find_element(By.ID, 'register-button').click()
    
        #implicit wait
        driver.implicitly_wait(5)
        respon = driver.find_element(By.CLASS_NAME, 'result').text #untuk validasi jika berhasil login apakah masuk ke page berikutnya
        self.assertIn('Your registration completed', respon) # yang mau kita cek: product ada di mana : respon
        
    def test_b_fail_regist(self): #no input email
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") #untuk menyimpan url mana yang akan di test 
        driver.maximize_window() #untuk memaksimalkan tampilan window 

        linkText = driver.find_element(By.CLASS_NAME,'ico-register')
        linkText.click()
        driver.find_element(By.ID, 'FirstName').send_keys('Coba') #inspek elemen by ID
        driver.find_element(By.ID, 'LastName').send_keys('Ini') 
        driver.find_element(By.ID, 'Email').send_keys('')
        driver.find_element(By.ID, 'Password').send_keys('iniiniini')
        driver.find_element(By.ID, 'ConfirmPassword').send_keys('iniiniini') 
        driver.find_element(By.ID, 'register-button').click()


        respon=driver.find_element(By.CLASS_NAME, 'field-validation-error').text
        self.assertIn('Email is required.', respon)
        #driver.minimize_window()
       



if __name__ == '__main__':
    unittest.main()