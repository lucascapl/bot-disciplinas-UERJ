from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from utils import getLoginCredentials, login, get_disciplinasRestantes, extract_data

options = Options()
options.add_experimental_option("detach", True)
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

matricula, senha = getLoginCredentials()

navegador.get("https://www.alunoonline.uerj.br/requisicaoaluno/")
navegador.maximize_window()

login(navegador, matricula, senha)

disciplinasRestantes = get_disciplinasRestantes(navegador)

dados = []
for linha in disciplinasRestantes:
    colunas = extract_data(linha)
    dados.append(colunas)

df = pd.DataFrame(dados, columns=["Disciplina", "Período", "Atendida?"])

print(df)

navegador.quit()
