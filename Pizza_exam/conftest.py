import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TestPizzaWebsite(webdriver):
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def teardown_class(self):
        self.driver.quit()

    def test_navigate_to_website(self):
        self.driver.get("https://atidcollege.co.il/Xamples/pizza/")
        assert "Pizza" in self.driver.title

    def test_delivery(self):
        f_name ='Edward'
        l_name ='Vishnivetzki'
        self.driver.find_element(By.CSS_SELECTOR, "#input_5_22_3").send_keys(f_name)
        self.driver.find_element(By.CSS_SELECTOR, "#input_5_22_6").send_keys(l_name)
        Select(self.driver.find_element(By.ID, "input_5_21")).select_by_value("Delivery|3")
        price = self.driver.find_element(By.XPATH, "//span[@class='ginput_total ginput_total_5']").text
        assert price == '$10.50'

    def test_apply_coupon(self):
        #locate the iframe of the coupon
        coupon = self.driver.find_element(By.XPATH, "//iframe[@src='coupon.html']")
        self.driver.switch_to.frame(coupon)
        #copy the coupon value
        coupon_number = self.driver.find_element(By.ID, "coupon_Number").text
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "input_5_20").send_keys(coupon_number)
