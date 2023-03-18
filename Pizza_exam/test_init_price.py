from selenium.webdriver.common.by import By

def test_navigate_to_website(driver):
    initial_price ='$7.50'
    driver.get("https://atidcollege.co.il/Xamples/pizza/")
    price = driver.find_element(By.XPATH, "//span[@class='ginput_total ginput_total_5']").text
    assert initial_price == price

