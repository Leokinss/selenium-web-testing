from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import os

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        s = Service('./chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

        # Delete Database if it exists
        path_to_db = '../website/database.db'
        if os.path.exists(path_to_db):
            os.remove(path_to_db)


    def test_signup(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/sign-up")
        print(driver.title)

        search_bar = driver.find_element(By.NAME, "email")
        search_bar.clear()
        search_bar.send_keys("test123@hotmail.com")

        search_bar = driver.find_element(By.NAME, "firstName")
        search_bar.clear()
        search_bar.send_keys("Joe")

        search_bar = driver.find_element(By.NAME, "password1")
        search_bar.clear()
        search_bar.send_keys("Password123!@#")

        search_bar = driver.find_element(By.NAME, "password2")
        search_bar.clear()
        search_bar.send_keys("Password123!@#")

        driver.find_element(By.NAME, "submit").click()

    def tearDown(self):
        #pass
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()