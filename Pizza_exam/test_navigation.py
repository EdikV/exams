def test_navigate_to_website(driver):
    driver.get("https://atidcollege.co.il/Xamples/pizza/")
    assert "Pizza" in driver.title