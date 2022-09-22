from gettext import find
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import time
from webdriver_manager.chrome import ChromeDriverManager


wb = load_workbook(filename="D:\Web\Python\exceltoweb\datakomen.xlsx")

sheetRange = wb['Sheet1']

driver = webdriver.Chrome()

driver.get("alamat web")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.implicitly_wait(20)

# looping input

i = 2
# for i in range(len(sheetRange['A'])):

if i <= len(sheetRange['A']):
    Nama = sheetRange['A'+str(i)].value
    Email = sheetRange['B'+str(i)].value
    Pesan = sheetRange['C'+str(i)].value



try:
    # WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="contact"]/div')))
    driver.find_element('id','name').send_keys(Nama)
    driver.find_element('id','email').send_keys(Email)
    driver.find_element('id','pesan').send_keys(Pesan)

    element = driver.find_element(By.XPATH, 'path button submit')
    element.submit()

except TimeoutException:
    print("input gagal")
    pass

time.sleep(10)
i = i + 1

print("data sudah di input")