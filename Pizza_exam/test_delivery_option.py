import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_delivery(driver):
    f_name ='Edward'
    l_name ='Vishnivetzki'
    driver.get("https://atidcollege.co.il/Xamples/pizza/")
    driver.find_element(By.CSS_SELECTOR, "#input_5_22_3").send_keys(f_name)
    driver.find_element(By.CSS_SELECTOR, "#input_5_22_6").send_keys(l_name)
    Select(driver.find_element(By.ID, "input_5_21")).select_by_value("Delivery|3")
    price = driver.find_element(By.XPATH, "//span[@class='ginput_total ginput_total_5']").text


    assert price == '$10.50'


    time.sleep(15)