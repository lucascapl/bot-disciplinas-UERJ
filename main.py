from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import sys
from utils import getLoginCredentials, login, get_disciplinasRestantes, extract_data

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

matricula, senha = getLoginCredentials()

driver.get("https://www.alunoonline.uerj.br/requisicaoaluno/")
driver.maximize_window()

login(driver, matricula, senha)

disciplinasRestantes = get_disciplinasRestantes(driver)

dados = []
for linha in disciplinasRestantes:
    colunas = extract_data(linha)
    dados.append(colunas)

df = pd.DataFrame(dados, columns=["Disciplina", "Período", "Atendida?", "Tipo", "Ramif.", "Cred.", "CH Total", "Trava credito"])

print(df)

sys.exit()
