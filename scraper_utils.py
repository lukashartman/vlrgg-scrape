from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data_utils import sanitize_map_name


def get_teams(driver):
    # Select div with class "match-header-vs-score"
    div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.match-header-vs"))
    )
    driver.execute_script("arguments[0].style.backgroundColor = 'orange'", div)

    # Get text of both divs with class "wf-title-med"
    team_elements = div.find_elements(By.CLASS_NAME, "wf-title-med")
    team_names = [team_element.text for team_element in team_elements]
    return team_names


def get_team_loadout(driver):
    # Pro play is max bo5
    map_loadouts = dict()

    # Find the element with data-tab="economy"
    economy_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-tab="economy"]'))
    )

    # Click on the element with data-tab="economy"
    economy_element.click()

    # Find all the items with class 'js-map-switch'
    map_switch_elements = driver.find_elements(By.CSS_SELECTOR, ".js-map-switch")

    # Loop through the map switch elements
    for map_switch_element in map_switch_elements[1:]:
        # Check if the data-disabled field is '1' instead of '0'
        data_disabled = map_switch_element.get_attribute("data-disabled")
        if data_disabled == "1":
            break  # Stop the loop if data-disabled is '1'

        # div within map_switch_element
        current_map = map_switch_element.find_element(By.CSS_SELECTOR, "div").text

        # Click on the map switch element
        map_switch_element.click()

        # select div with padding of 20px 0 within div with class "vm-stats-game"
        # wait for element to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.vm-stats-game > div[style='padding: 20px 0; overflow-x: auto;']"))
        )
        div = driver.find_element(By.CSS_SELECTOR,
                                  "div.vm-stats-game > div[style='padding: 20px 0; overflow-x: auto;']")

        # scroll to div
        driver.execute_script("arguments[0].scrollIntoView();", div)

        # select first table within table_element
        table_element = div.find_element(By.CSS_SELECTOR, "table")
        driver.execute_script("arguments[0].style.backgroundColor = 'orange'", div)

        # find tbody element, then tr element, then td element of table_element
        round_elements = table_element.find_elements(By.CSS_SELECTOR, "td")

        bank_values = []

        # loop through all td elements
        for round_element in round_elements:
            # check if div has class "bank"
            if round_element.find_elements(By.CLASS_NAME, "round-num"):
                team_a = round_element.find_element(By.CLASS_NAME, "bank").text
                team_b = round_element.find_element(By.CLASS_NAME, "bank").text
                win_lose = get_score(round_element)
                bank_values.append(((team_a, team_b), win_lose))
                driver.execute_script("arguments[0].style.backgroundColor = 'green'", round_element)
        map_loadouts.update({sanitize_map_name(current_map): bank_values})

        # print bank values
    return map_loadouts


def get_score(round_element):
    winner_encode = round_element.find_element(By.CLASS_NAME, "rnd-sq").get_attribute("class")

    if "t" in winner_encode:
        return True, False
    else:
        return False, True
