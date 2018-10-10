import pytest

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    # global driver
    driver = webdriver.Chrome(
        executable_path="C:/Users/Administrator/PycharmProjects/AutomationFrameworkPractice_1/drivers/chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")