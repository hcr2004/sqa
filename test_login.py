from appium import webdriver
from appium.options.common import AppiumOptions
import time

# BrowserStack credentials
USERNAME = "disharao_uM6q18"
ACCESS_KEY = "Uxi86VgHAHo9CWwqsp3S"

# Desired capabilities
caps = {
    "platformName": "Android",
    "deviceName": "Samsung Galaxy S21",
    "os_version": "11.0",
    "app": "bs://bd814c27814f88c6119feaa1670af2a737dbb492",
    "project": "Expense Tracker App",
    "build": "Python Appium Build",
    "name": "Login Functionality Test",
    "browserstack.debug": True,
    "browserstack.networkLogs": True,
    "browserstack.appium_version": "2.0.1"
}

# Setup driver
options = AppiumOptions()
options.load_capabilities(caps)

driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
    options=options
)

print("✅ App launched successfully on BrowserStack!")

try:
    # Locate elements using the IDs from your Java code
    email_field = driver.find_element('id', 'com.example.expensetracker:id/email_login')
    password_field = driver.find_element('id', 'com.example.expensetracker:id/password_login')
    login_button = driver.find_element('id', 'com.example.expensetracker:id/btn_login')

    # Input credentials
    email_field.send_keys("testuser@example.com")
    password_field.send_keys("password123")

    # Tap the login button
    login_button.click()

    time.sleep(5)  # wait for next activity to load

    # Check for successful login by verifying a view from HomeActivity (update this ID as needed)
    success_element = driver.find_element('id', 'com.example.expensetracker:id/home_text')  # Update with a real ID

    if success_element:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Login successful and HomeActivity opened"}}')
        print("✅ Login test passed")
    else:
        raise Exception("Home screen element not found after login")

except Exception as e:
    print("❌ Test failed:", e)
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Login failed or navigation error"}}')

finally:
    driver.quit()
    print("🚀 Test session ended.")
