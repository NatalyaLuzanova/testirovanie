import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открыть сайт и залогиниться
s = Service('C:/Test/Chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login")
driver.set_window_size(1024, 800)
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("nata.luzanova@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)

# Открыть форму паспорта
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
# Заполнение формы
driver.find_element(By.ID, "surname").clear()
driver.find_element(By.ID, "surname").send_keys("Лузанова")
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Наталья")
driver.find_element(By.ID, "patronymic").clear()
driver.find_element(By.ID, "patronymic").send_keys("Игоревна")
driver.find_element(By.NAME, "date").click()
date = "18 марта 2022"
month_year = "март 2022"
for c in range(12):
    month = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/span").text
    if month == month_year:
        days = driver.find_elements(By.CSS_SELECTOR, ".mx-date-row:nth-child(2) > .cell:nth-child(3) > div")
        for i in days:
            if i.get_attribute("title") == ("2022-03-18"):
                i.click()
                time.sleep(1)
                break
        break
    else:
        arrow_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/button[2]")
        arrow_button.click()
        time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/table/tbody/tr[3]/td[5]").click()

driver.find_element(By.CSS_SELECTOR, "#passportSeries").clear()
driver.find_element(By.CSS_SELECTOR, "#passportSeries").send_keys("1357")
driver.find_element(By.CSS_SELECTOR, "#passportNumber").clear()
driver.find_element(By.CSS_SELECTOR, "#passportNumber").send_keys("487898")

driver.find_element(By.ID, "dateOfIssue").click()
date1 = "1 март 2022"
month_year1 = "март 2022"
for d in range(12):
    month1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/span").text
    if month1 == month_year1:
        days1 = driver.find_elements(By.CSS_SELECTOR, ".mx-date-row:nth-child(3) > .cell:nth-child(3) > div")
        for k in days1:
            if k.get_attribute("title") == ("2022-03-01"):
                k.click()
                time.sleep(1)
                break
        break
    else:
        arrow_button1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/button[2]")
        arrow_button1.click()
        time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/table/tbody/tr[3]/td[5]").click()

driver.find_element(By.CSS_SELECTOR, "#code").clear()
driver.find_element(By.CSS_SELECTOR, "#code").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "#cardId").clear()
driver.find_element(By.CSS_SELECTOR, "#cardId").send_keys("67590789000")
driver.find_element(By.CSS_SELECTOR, "#issued").clear()
driver.find_element(By.CSS_SELECTOR, "#issued").send_keys("МВД г. Владивостока")
# Адрес
address = driver.find_element(By.XPATH, "//*[@id='address']/div/div/input")

address.send_keys(Keys.CONTROL + "a")
address.send_keys(Keys.DELETE)
address.send_keys("г Керчь, ул Ленина, д 23")
address.click()
wait = WebDriverWait(driver, 2)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'vue-dadata__suggestions')))
address.send_keys(Keys.ARROW_DOWN)
address.send_keys(Keys.ENTER)
time.sleep(4),

driver.find_element(By.ID, 'phone').send_keys(Keys.CONTROL + "a")
driver.find_element(By.ID, 'phone').send_keys(Keys.DELETE)
driver.find_element(By.ID, 'phone').send_keys("9991234567")
filePath ='C:\\Test\\4cats.jpg'
driver.find_element(By.CSS_SELECTOR, '#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div.form.passport-form.document-form > div.body > div.upload-widget.upload-widget > input[type=file]').send_keys(filePath)
time.sleep(5)
driver.find_element(By.XPATH, "//div[@id='__layout']/div/div[3]/div/div/div[3]/div/div/div[2]/div[3]/div[9]/button[2]").click()




