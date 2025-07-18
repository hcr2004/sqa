from appium import webdriver
from appium.options.common import AppiumOptions
import time

# BrowserStack credentials
USERNAME = "disharao_uM6q18"
ACCESS_KEY = "Uxi86VgHAHo9CWwqsp3S"

# Capabilities
caps = {
    "platformName": "Android",
    "deviceName": "Samsung Galaxy S21",
    "os_version": "11.0",
    "app": "bs://bd814c27814f88c6119feaa1670af2a737dbb492",
    "project": "Expense Tracker App",
    "build": "Python Appium Build",
    "name": "Forgot Password - Invalid Email",
    "browserstack.debug": True,
    "browserstack.networkLogs": True,
    "browserstack.appium_version": "2.0.1"
}

# Appium driver setup
options = AppiumOptions()
options.load_capabilities(caps)

driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
    options=options
)

try:
    print("✅ App launched. Navigating to Forgot Password screen...")

    # Go to ForgotPasswordActivity
    forgot_button = driver.find_element("id", "com.example.expensetracker:id/forget_password")
    forgot_button.click()
    time.sleep(2)

    # Leave email field empty
    reset_button = driver.find_element("id", "com.example.expensetracker:id/btn_reset_password")
    reset_button.click()

    time.sleep(2)

    # Check for error text
    error = driver.find_element("xpath", "//*[@text='Failed to send reset email.']")
    if error:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Empty email validation works."}}')
        print("✅ Empty email test passed.")
    else:
        raise Exception("Error message not shown.")

except Exception as e:
    print("❌ Test failed:", e)
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Validation error not shown for empty input."}}')

finally:
    driver.quit()
