# # do not use, still under development
# # can start multiple drivers all at once, can freeze the computer
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchWindowException, WebDriverException
# import pandas as pd
# import time
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
#
# square_dictionary = {"a" : "1", "b" : "2", "c" : "3", "d" : "4", "e" : "5", "f" : "6", "g" : "7", "h" : "8"}
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#
# # selenium
# driver.get("https://www.chess.com/puzzles/rated")
#
# # close button
# button = driver.find_element(By.XPATH, '''//*[@id="first-time-modal"]/div/div[2]/div/button/div''')
# button.click()
#
# # hint button
# time.sleep(3)
# hint_button = driver.find_element(By.XPATH, '''//*[@id="sidebar"]/section/div/div[3]/div[1]/button''')
# hint_button.click()
# hint_button.click()
# hint_button.click()
#
# # answer
# answer = driver.find_elements(By.XPATH, '''//*[contains(@id, "arrow-")]''')
# answer_move = ""
# for a in answer:
#     answer_move = a.get_attribute("id").split("-")[1]
#
# target_square_number = f"square-{square_dictionary[answer_move[0]]+answer_move[1]}"
#
# board_primary = driver.find_element(By.ID, 'board-primary')
# child_elements = board_primary.find_elements(By.XPATH, './child::*')
# target = None
# for child in child_elements:
#     if target_square_number in child.get_attribute("class"):
#         target = child
# target.click()
#
# # destination
# destination_square_number = f"square-{square_dictionary[answer_move[2]]+answer_move[3]}"
# elements = driver.find_elements(By.XPATH, f"//*[contains(@class, '{destination_square_number}')]")
# for element in elements:
#     if "piece" in element.get_attribute("class"):
#         element.click()
#         break
#
#
# # destination
# test = input("Enter the number of games you want to play: ")
# # target
# # c = 3, so 34
#
# # # elements
# # board_primary = driver.find_element(By.ID, 'board-primary')
# # child_elements = board_primary.find_elements(By.XPATH, './child::*')
# # # target square
# # target_string = child_elements[1].get_attribute("class").split("-")[1]
# # target_class = f"piece wb square-{target_string}"
# # target_square = None
# # for child in child_elements:
# #     if child.get_attribute("class") == target_class:
# #         target_square = child
# #         break
# #
# # target_square.click()
# #
# # # destination
# # board_primary = driver.find_element(By.ID, 'board-primary') # pulling list again
# # child_elements = board_primary.find_elements(By.XPATH, './child::*')
# # possible_destinations = []
# # for child in child_elements:
# #     if child.get_attribute("data-test-element") == "hint":
# #         possible_destinations.append(child)
# #
# # possible_destinations[1].click()
# # possible_destinations[0].click()
# # target_square = driver.find_element(By.XPATH, //*[@id="board-primary"]/div[8])
# # target_square.click()
#
#
#
#
# # answer //*[@id="arrow-c4d5"]