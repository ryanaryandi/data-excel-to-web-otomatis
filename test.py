from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Menjalankan Web Browser
browser  = webdriver.Chrome()

# Membuka Website Shopee
browser.get('https://shopee.co.id/buyer/login?next=https%3A%2F%2Fshopee.co.id%2F')
browser.maximize_window()
# Interaksi Otomatis
# Email dan Password Shopee
email = "EMAIL"
password = "PASSWORD"

# Mengisi Email dan Password

browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/div[2]/div[1]/input').send_keys(email)
browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/div[3]/div[1]/input').send_keys(password)

# browser.find_element_by_css_selector("._1HkukX ._56AraZ").send_keys(email)
# browser.find_element_by_css_selector("._3Uo2e7 ._56AraZ").send_keys(password)

# Klik Log In
element = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/button')
element.click()

time.sleep(20)
i = i + 1

print("data sudah di input")
    