import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# selenium
driver.get("https://www.chess.com/puzzles/rated")
i = 1
while True:
    # destination
    test = input("Enter to continue....")
    if test == "exit":
        driver.close()
        break

    # download button
    download_button = driver.find_element(By.XPATH, '''//*[@id="sidebar"]/section/div/div[5]/div/div[1]/button[3]''')
    download_button.click()

    # confirm download
    time.sleep(1)
    confirm_download = driver.find_element(By.XPATH, '''//*[@id="share-modal"]/div/div[2]/div/section/div[1]/button''')
    confirm_download.click()

    # close dialog
    close_dialog = driver.find_element(By.XPATH, '''//*[@id="share-modal"]/div/div[2]/button''')
    close_dialog.click()

    # info
    print(f"[INFO] Game {i} downloaded")
    i+=1