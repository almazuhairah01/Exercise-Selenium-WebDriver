import pytest
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait #explicit waits
from selenium.webdriver.support import expected_conditions as EC
from locator import elem #untuk locator 
from datainputan import inputan #untuk inputan 


class TestRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
	
    def test_a_success_regist(self):
        driver = self.driver
        driver.get(inputan.url) 
        driver.maximize_window() #untuk memaksimalkan tampilan window 

        linkText = driver.find_element(By.CLASS_NAME,'ico-register')
        linkText.click()
        driver.find_element(By.ID, elem.FirstName).send_keys('tiga') #inspek elemen by ID
        driver.find_element(By.ID, elem.LastName).send_keys('tiga') 
        driver.find_element(By.ID, elem.email).send_keys('tiga333@gmail.com')
        driver.find_element(By.ID, elem.passw).send_keys('duadua22')
        driver.find_element(By.ID, elem.confirmPass).send_keys('duadua22') 
        driver.find_element(By.ID, elem.buttReg).click()
    
        #implicit wait
        driver.implicitly_wait(5)
        respon = driver.find_element(By.CLASS_NAME, 'result').text #untuk validasi jika berhasil login apakah masuk ke page berikutnya
        self.assertIn('Your registration completed', respon) # yang mau kita cek: product ada di mana : respon
        
    def test_b_fail_regist(self): #no input email
        driver = self.driver
        driver.get(inputan.url) #untuk menyimpan url mana yang akan di test 
        driver.maximize_window() #untuk memaksimalkan tampilan window 

        linkText = driver.find_element(By.CLASS_NAME,'ico-register')
        linkText.click()
        driver.find_element(By.ID, elem.FirstName).send_keys('Coba') #inspek elemen by ID
        driver.find_element(By.ID, elem.LastName).send_keys('Ini') 
        driver.find_element(By.ID, elem.email).send_keys('')
        driver.find_element(By.ID, elem.passw).send_keys('iniiniini')
        driver.find_element(By.ID, elem.confirmPass).send_keys('iniiniini') 
        driver.find_element(By.ID, elem.buttReg).click()


        respon=driver.find_element(By.CLASS_NAME, 'field-validation-error').text
        self.assertIn('Email is required.', respon)
        #driver.minimize_window()
       



if __name__ == '__main__':
    unittest.main()