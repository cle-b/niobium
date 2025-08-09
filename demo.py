from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import niobium
import time

# Adresse de ton hub Selenium
HUB_URL = "http://localhost:4444/wd/hub"

# Options Chrome (facultatif)
options = Options()

# Création du driver remote
driver = webdriver.Remote(command_executor=HUB_URL,options=options)

# Exemple d'utilisation
driver.get("https://google.com")
print(driver.title)
time.sleep(2)
driver.find_element(By.IMAGE, "googlestore.png").click()
time.sleep(5)
print(driver.title)


driver.quit()