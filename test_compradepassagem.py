import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Driver instanciado corretamente
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class TestCompradepassagem():
    def setup_method(self, method):
        # Utiliza o mesmo serviço de ChromeDriver instanciado acima
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_compradepassagem(self):
        self.driver.get("https://www.blazedemo.com/")
        self.driver.set_window_size(1536, 834)
        self.driver.find_element(By.NAME, "fromPort").click()
        dropdown = self.driver.find_element(By.NAME, "fromPort")
        dropdown.find_element(By.XPATH, "//option[. = 'São Paolo']").click()
        self.driver.find_element(By.NAME, "toPort").click()
        dropdown = self.driver.find_element(By.NAME, "toPort")
        dropdown.find_element(By.XPATH, "//option[. = 'New York']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.ID, "inputName").send_keys("ELIEL DE OLIVEIRA DANTAS")
        self.driver.find_element(By.ID, "address").send_keys("Rua Padre Miguel De Campos")
        self.driver.find_element(By.ID, "city").send_keys("São Paulo")
        self.driver.find_element(By.ID, "state").send_keys("SP")
        self.driver.find_element(By.ID, "zipCode").send_keys("03568-050")
        self.driver.find_element(By.ID, "cardType").click()
        dropdown = self.driver.find_element(By.ID, "cardType")
        dropdown.find_element(By.XPATH, "//option[. = 'Diner\'s Club']").click()
        self.driver.find_element(By.ID, "rememberMe").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Thank you for your purchase today!"
