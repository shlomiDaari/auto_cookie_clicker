from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\chromedriver.exe"  # path to the webdriver
driver = webdriver.Chrome(PATH) 
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookieCount = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]


actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookieCount.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions = actions.move_to_element(item)
            upgrade_actions = actions.click()
            upgrade_actions = actions.perform()

