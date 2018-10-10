# CONSTANTS
import inspect

URL         =   "https://opensource-demo.orangehrmlive.com/"
USERNAME    =   "Admin"
PASSWORD    =   "admin123"

def save_screenshot(driver, name):
    driver.get_screenshot_as_file("C:/Users/Administrator/PycharmProjects/AutomationFrameworkPractice_1/screenshots/" + name + ".png")

def whoami():
    return inspect.stack()[1][3]