# ganesha the great
import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
 
driver.get("https://linkedin.com")
while "1" != input("press 1 when signed in: "):
    pass
driver.get("https://www.linkedin.com/mynetwork/")
sleep(4)
buttons=driver.find_elements_by_xpath('//button[@class="invitation-card__action-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view"]')
for button in buttons:
    word=button.get_attribute("aria-label")
    if word.split(" ")[0] == "Accept":
        print("clicking...")
        button.click()
        print("click")
        sleep(10)
driver.close()