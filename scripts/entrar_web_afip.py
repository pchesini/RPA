from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time

# Cargar .env
load_dotenv()
CUIT = os.getenv("AFIP_CUIT")
PASS = os.getenv("AFIP_PASS")

if not CUIT or not PASS:
    raise RuntimeError("⚠️ No se encontraron variables AFIP_CUIT y AFIP_PASS en .env")

# Configurar navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)

# Ir a login AFIP
driver.get("https://auth.afip.gob.ar/contribuyente_/login.xhtml")

# Ingresar CUIT
cuit_input = wait.until(EC.presence_of_element_located((By.ID, "F1:username")))
cuit_input.send_keys(CUIT)
driver.find_element(By.ID, "F1:btnSiguiente").click()

# Ingresar clave
clave_input = wait.until(EC.presence_of_element_located((By.ID, "F1:password")))
clave_input.send_keys(PASS)
driver.find_element(By.ID, "F1:btnIngresar").click()

time.sleep(5)
print("✅ Login realizado con éxito")