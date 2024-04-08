from selenium.webdriver.common.by import By

def getLoginCredentials():
    with open('config.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            if key == 'matricula':
                matricula = value
            elif key == 'senha':
                senha = value
    return matricula, senha

def login(driver, matricula, senha):
    campoMatricula = driver.find_element(By.ID, "matricula")
    campoSenha = driver.find_element(By.ID, "senha")

    campoMatricula.send_keys(matricula)
    campoSenha.send_keys(senha)

    botaoEntrar = driver.find_element(By.CLASS_NAME, "botao")
    botaoEntrar.click()

def get_disciplinasRestantes(driver):
    elemento = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/form/table/tbody/tr[4]/td[3]/div[2]/div[3]/a')
    elemento.click()

    linhasTabelaCompleta = driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[3]/td/form/div[1]/div[2]/table//tr')
    disciplinasRestantes = []

    for linha in linhasTabelaCompleta[1:]:
        colunaAtendida = linha.find_element(By.XPATH, './td[3]')
        colunaObrigatoria = linha.find_element(By.XPATH, './td[4]')

        if colunaAtendida.text.strip().lower() == "não" and colunaObrigatoria.text.strip().lower() == "obrigatória":
            disciplinasRestantes.append(linha)

    return disciplinasRestantes

def extract_data(linha):
    colunas = []
    for i in range(1, 9):
        colunas.append(linha.find_element(By.XPATH, f'./td[{i}]').text.strip())
    return colunas