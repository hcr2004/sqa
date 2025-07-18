from appium import webdriver
from appium.options.common import AppiumOptions
import time

# ✅ Your BrowserStack credentials
USERNAME = "disharao_uM6q18"
ACCESS_KEY = "Uxi86VgHAHo9CWwqsp3S"

# ✅ BrowserStack capabilities
caps = {
    "platformName": "Android",
    "deviceName": "Samsung Galaxy S21",
    "os_version": "11.0",
    "app": "bs://bd814c27814f88c6119feaa1670af2a737dbb492",  # Make sure this is your latest uploaded app
    "project": "Expense Tracker App",
    "build": "Python Appium Build",
    "name": "Logout Test",

    # ✅ Enable video & logs for debug
    "browserstack.debug": True,
    "browserstack.networkLogs": True,
    "browserstack.appium_version": "2.0.1"
}

# ✅ Load into AppiumOptions
options = AppiumOptions()
options.load_capabilities(caps)

# ✅ Create driver with auth
driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
    options=options
)

try:
    menu_button = driver.find_element("accessibility id", "Open navigation drawer")
    menu_button.click()
    time.sleep(2)

    logout_button = driver.find_element("id", "com.example.expensetracker:id/logout")
    logout_button.click()
    time.sleep(2)

    # Check if redirected to login screen (MainActivity)
    login_btn = driver.find_element("id", "com.example.expensetracker:id/btn_login")
    assert login_btn.is_displayed()

    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Logout successful and redirected to login screen."}}')
    print("✅ Logout test passed.")
except Exception as e:
    print("❌", e)
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Logout failed or did not redirect."}}')
