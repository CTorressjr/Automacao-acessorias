import pandas as pd
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
WebDriverWait(driver, 10)
url = 'https://app.acessorias.com/sysmain.php?m=4'
driver.get(url)
driver.maximize_window()


pyautogui.PAUSE = 1.5
pyautogui.write("joas@controllersbr.com")
pyautogui.press("tab")
pyautogui.write("Senha@005570")
pyautogui.press("tab")
pyautogui.press("enter")   
driver.find_element(By.XPATH, '//*[@id="M4"]/a/span/nobr').click() #clica em empresas
time.sleep(2)
pyautogui.typewrite("medicalmais")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="btFilter"]').click() #clica em filtrar
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="divEmpZ_684"]/div[1]/span[1]').click()


tabela = pd.read_csv(r"C:\Users\Winlitepro\Desktop\Inclusão de outros identificadores\CNPJMAT.csv")


actions = ActionChains(driver)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="spanNewInscZ"]'))
)
actions.double_click(element).perform() #abre nome do identificador

def criaidentificador():
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="EmpNewInscZ"]').click()
    scp = tabela.loc[linha, "CNPJ"]
    pyautogui.write(str(tabela.loc[linha, "CNPJ"]))
    pyautogui.press("tab") #seleciona campo nome do identificador
    pyautogui.write("SCP ")
    scp = tabela.loc[linha, "SCP"]
    pyautogui.write(str(tabela.loc[linha, "SCP"]))
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="EmpIncsz"]/div[1]/div[2]/a/i').click()
    time.sleep(1)
   # driver.find_element(By.XPATH, '//*[@id="navIni"]').click()

for linha in tabela.index:
    criaidentificador()

driver.find_element(By.XPATH, '//*[@id="btSalvar"]').click()
time.sleep(5)   

