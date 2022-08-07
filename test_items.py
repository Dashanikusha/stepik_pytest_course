from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button(browser):
    browser.get(link)
    time.sleep(30)
    items = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(items) > 0, 'Cелектор кнопки не найден'

