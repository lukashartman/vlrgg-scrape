from selenium import webdriver

from data_utils import *
from scraper_utils import *

driver = webdriver.Firefox()
driver.get("https://www.vlr.gg/matches/results")
match_elements = driver.find_elements(By.CSS_SELECTOR, "a.wf-module-item")
for match_element in match_elements:
    # open the link in a new tab and switch to it
    driver.execute_script("window.open(arguments[0], '_blank')", match_element.get_attribute("href"))
    driver.switch_to.window(driver.window_handles[1])

    team_names = get_teams(driver)
    print(team_names)

    team_loadouts = get_team_loadout(driver)
    print(team_loadouts)

    team_a_data = rectify_team_data(team_loadouts, team_names[0], team_names[1])
    print(team_a_data)

    # Go back to the desired page and close the opened tab
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.wf-module-item")))
driver.quit()


