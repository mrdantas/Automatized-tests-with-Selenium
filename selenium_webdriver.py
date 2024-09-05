# Configura

# Import
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest




# Dados de Entrada
url= 'https://www.blazedemo.com/'
# origem = 'São Paolo'
# destino = 'New York'
primeiro_nome = 'Juca'
bandeira = 'American Express'
lembrar_de_mim = True

# Resultados Esperados
titulo_passagens_esperado = 'Flights from São Paolo to New York:'
mensagem_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'

# Executa
class Testes:

    # Driver instanciado corretamente
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Inicio
    def setup_method(self):
        # Instanciar a biblioteca/motor/engine
        # Informar onde está o webdriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        # espera até 15 segundos por qualquer elemento
        self.driver.implicitly_wait(15)

    # Fim
    def teardown_method(self):
        # Destruir o objeto da biblioteca utilizado
        self.driver.quit()

    # Meio
    lista_de_valores = [
        ('São Paolo', 'New York'),
        ('Boston', 'Berlin'),
        ('San Diego', 'New York'),
    ]

    @pytest.mark.parametrize('origem,destino', lista_de_valores)
    def testar_comprar_passagem(self, origem, destino):
        # e2e / end to end / ponta a ponta
        
        # Pagina inicial (Home)
        # Executa / Valida
        self.driver.get(url)
        
        # Departure city
        lista = self.driver.find_element(By.NAME, 'fromPort')
        lista.click()
        lista.find_element(By.XPATH, f'//option[contains(text(), "{origem}")]').click()

        # Destination city
        lista = self.driver.find_element(By.NAME, 'toPort')
        lista.click()
        lista.find_element(By.XPATH, f'//option[contains(text(), "{destino}")]').click()

        # Find flights
        self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()

        # Pagina Lista de passagens
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.TAG_NAME, 'h3'))
        # )
        assert self.driver.find_element(By.TAG_NAME, 'h3').text == titulo_passagens_esperado

        # Selecionar o primeiro voo
        self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) .btn').click()

        #Pagina de compra

        #Pagina de obrigado  

        #Executa

# Valida