from appium import webdriver
from appium.options.common import AppiumOptions
import time

# ✅ BrowserStack credentials
USERNAME = "disharao_uM6q18"
ACCESS_KEY = "Uxi86VgHAHo9CWwqsp3S"

# ✅ App and device capabilities
caps = {
    "platformName": "Android",
    "deviceName": "Samsung Galaxy S21",
    "os_version": "11.0",
    "app": "bs://bd814c27814f88c6119feaa1670af2a737dbb492",
    "project": "Expense Tracker App",
    "build": "Python Appium Build",
    "name": "Open Navigation Drawer Test",
    "browserstack.debug": True,
    "browserstack.networkLogs": True,
    "browserstack.appium_version": "2.0.1"
}

# ✅ Appium options
options = AppiumOptions()
options.load_capabilities(caps)

# ✅ Start session with BrowserStack
driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
    options=options
)

# Wait for the app to load HomeActivity (after login)
time.sleep(5)

try:
    # ✅ Locate and tap the navigation drawer (hamburger) icon
    menu_button = driver.find_element("accessibility id", "Open navigation drawer")
    menu_button.click()
    print("✅ Navigation drawer opened successfully.")

    # ✅ Mark test passed on BrowserStack
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Navigation drawer opened."}}')

except Exception as e:
    print(f"❌ Failed to open navigation drawer: {e}")
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Navigation drawer not found."}}')

# End session
driver.quit()
