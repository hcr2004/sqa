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
    "name": "Registration Test",

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

print("✅ Connected to BrowserStack and app launched!")

try:
    # Let app load
    time.sleep(5)

    # ✅ Mark test as passed on BrowserStack
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "App launched successfully"}}')
    print("✅ Marked test as passed on BrowserStack.")

except Exception as e:
    # ❌ If something fails, mark test as failed
    driver.execute_script(f'browserstack_executor: {{"action": "setSessionStatus", "arguments": {{"status":"failed","reason": "{str(e)}"}}}}')
    print(f"❌ Test failed: {e}")

finally:
    # Quit session
    driver.quit()
    print("🚀 Test completed and session ended.")
