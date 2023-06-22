from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scraper_utils import get_team_loadout


driver = webdriver.Firefox()
driver.get("https://www.vlr.gg/matches/results")
match_elements = driver.find_elements(By.CSS_SELECTOR, "a.wf-module-item")
for match_element in match_elements:
    # open the link in a new tab and switch to it
    driver.execute_script("window.open(arguments[0], '_blank')", match_element.get_attribute("href"))
    driver.switch_to.window(driver.window_handles[1])

    print(get_team_loadout(driver))

    # Go back to the desired page and close the opened tab
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.wf-module-item")))
driver.quit()


