from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class Test_Synchronization:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
    def teardown_class(cls):
        driver.quit()

    def test_navigate_to_website(self):
        initial_price = '$7.50'
        driver.get("https://atidcollege.co.il/Xamples/pizza/")
        price = driver.find_element(By.XPATH, "//span[@class='ginput_total ginput_total_5']").text
        assert "Pizza" in driver.title
        assert initial_price == price

#    def test_delivery(self):
        f_name ='Edward'
        l_name ='Vishnivetzki'
        driver.find_element(By.CSS_SELECTOR, "#input_5_22_3").send_keys(f_name)
        driver.find_element(By.CSS_SELECTOR, "#input_5_22_6").send_keys(l_name)
        Select(driver.find_element(By.ID, "input_5_21")).select_by_value("Delivery|3")
        price = driver.find_element(By.XPATH, "//span[@class='ginput_total ginput_total_5']").text
        assert price == '$10.50'

#   def test_apply_coupon(self):
#        driver.get("https://atidcollege.co.il/Xamples/pizza/")
        # locate the iframe of the coupon
        coupon = driver.find_element(By.XPATH, "//iframe[@src='coupon.html']")
        driver.switch_to.frame(coupon)
        # copy the coupon value
        coupon_number = driver.find_element(By.ID, "coupon_Number").text
        driver.switch_to.default_content()
        driver.find_element(By.ID, "input_5_20").send_keys(coupon_number)

        driver.find_element_by_xpath("//input[@value='Submit Your Order']").click()
        popup=driver.switch_to.alert
        popup_text=popup.text
        assert popup_text==(f_name +" "+ l_name +" "+ str(coupon_number))  # Close the pop-up
        popup.accept()  # Close the pop-up


