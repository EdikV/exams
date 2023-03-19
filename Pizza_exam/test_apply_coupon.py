import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_apply_coupon(driver):
    driver.get("https://atidcollege.co.il/Xamples/pizza/")
    #locate the iframe of the coupon
    coupon=driver.find_element(By.XPATH,"//iframe[@src='coupon.html']")
    driver.switch_to_frame(coupon)
    #copy the coupon value
    coupon_number=driver.find_element(By.ID, "coupon_Number").text
    driver.switch_to_default_content()
    driver.find_element(By.ID, "input_5_20").send_keys(coupon_number)

    time.sleep(15)