# Automatized tests with Selenium e Robot Framework

## Passo a passo de como funcionar a automação:

### 1° - Instanciar o webdriver_manager no código

from webdriver_manager.chrome import ChromeDriverManager

Driver instanciado corretamente
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

### 2° - Verifique a versão do pip no bash - se não houver pip, instale.

pip --version

Para atualização:
pip install --upgrade pip

### 3° - Criar um ambiente virtual para isolar as dependências

python -m venv nome_do_ambiente

### 3.5° - Ativação windows:
nome_do_ambiente\Scripts\activate

### 3.6° - Ativação bash:
source nome_do_ambiente/Scripts/activate

### 3.7° - Para desativação do ambiente virtual:
deactivate

### 4° - Instalar as bibliotecas necessárias:

pip install pytest selenium webdriver-manager

### 5° - Crie o arquivo de teste:

- No seu editor de texto preferido (como VS Code), crie um arquivo chamado `test_nomedoseuteste.py`.

### 6° - Rode o teste usando o terminal, no diretório onde contém o arquivo:

pytest test_compradepassagem.py 