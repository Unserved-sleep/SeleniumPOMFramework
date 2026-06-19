from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
def test_login(setup):

    logger = LogGen.loggen()
    logger.info("Browser Launched")

    driver = setup
    driver.get("https://www.saucedemo.com")

    logger.info("URL Opened")

