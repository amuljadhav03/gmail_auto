import pytest

@pytest.fixture(scope='class')

def test_navi(request):
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:/Users/amul.kumar.PTW-I/PycharmProjects/gmail_auto/drivers/chromedriver.exe")
    driver.get("https://accounts.google.com/ServiceLogin/identifier?")
    driver.implicitly_wait(30)
    request.cls.driver = driver
