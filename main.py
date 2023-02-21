from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())


browser = webdriver.Chrome(service=service)

browser.get("https://www.obilet.com/")
browser.maximize_window()

ucak_tab = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'UÇAK')]")))
ucak_tab.click()

nereden_input = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='nereden']")))
nereden_input.send_keys("Sabiha Gökçen")
nereye_input = browser.find_element_by_xpath("//input[@name='nereye']")
nereye_input.send_keys("Antalya")

ara_button = browser.find_element_by_xpath("//button[contains(text(),'Ara')]")
ara_button.click()

try:
    havalimani_results = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Havalimanları')]")))
except:
    
    alert("Havalimanlari sonucu yüklenemedi!")
    browser.quit()
    exit()

havalimani_options = browser.find_elements_by_xpath(
    "//div[@class='cityairport-list-container']/ul/li")
for option in havalimani_options:
    if "Havalimanları" in option.text:
        option.click()
        break

tarihler_tab = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Tarihler')]")))
tarihler_tab.click()

gidis_tarihi_input = browser.find_element_by_xpath(
    "//input[@name='gidisTarihi']")
gidis_tarihi_input.send_keys("08/08/2023")

donus_tarihi_input = browser.find_element_by_xpath(
    "//input[@name='donusTarihi']")
donus_tarihi_input.send_keys("10/08/2023")

yolcu_tab = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Yolcu')]")))
yolcu_tab.click()

yetiskin_select = browser.find_element_by_xpath("//select[@name='yetiskin']")
yetiskin_select.click()
yetiskin_option = browser.find_element_by_xpath("//option[@value='1']")
yetiskin_option.click()

ara_button.click()

try:
    WebDriverWait(browser, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='flight-details clearfix']")))
except:
    alert("Uçuşlar listesi yüklenemedi!")
    browser.quit()
    exit()

