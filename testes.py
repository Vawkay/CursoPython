from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Instanciar web driver
driver = webdriver.Chrome(service=Service())
# abrir site google

#%%
driver.get('https://www.google.com.br/')

webdriver_version = driver.capabilities['browserVersion']

print("Versão do WebDriver:", webdriver_version)

#%%
driver.get('https://www.youtube.com.br/')

