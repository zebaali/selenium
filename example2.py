from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

domain = 'https://generator.email/'
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def prepare_driver():
    '''Returns a Chrome Webdriver.'''
    driver = Chrome('/Users/shivendra/Downloads/chromedriver')
    return driver

def run():
    d = prepare_driver()
    d.get("http://164.52.196.121/")
    element = d.find_element_by_id("freeTextSearch")
    element.send_keys("asia")
    element.send_keys(Keys.ENTER)
    d.quit()

def login2():
    try:
        d = prepare_driver()
        d.get("http://164.52.196.121/")
        d.maximize_window()
        click_btn = d.find_element_by_xpath('//*[@id="navbarContent"]/ul/li[6]/button').click()
        email = d.find_element_by_id("email").send_keys("zeba.ali@ezeiatech.in")
        passw = d.find_element_by_id("pwd").send_keys("zebaali")
        login_btn = d.find_element_by_id("login_continue").click()
        # if (d.find_element_by_xpath('//*[@id="dropdownMenuButton"]/a/span')):
        #     print("logged in")
        logged_in_success = WebDriverWait(d, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="dropdownMenuButton"]/a/span')))
        if logged_in_success:
            print ("login success")

        #act_click = d.find_element_by_id("activity__select").click()
        act_select = Select(d.find_element_by_id("activity__select"))
        act_select.select_by_value("backpacking")
        print("Task completed")
        mission_select = d.find_element_by_xpath('//*[@id="carouselExampleIndicators"]/div/div[7]/div[2]/span/div/button').click()
        #mission_select.select_by_visible_text("Long Holidays")
        #print("Long holidays select")
        #mission_select.select_by_visible_text("Day Trips")
        d.find_element_by_xpath('//*[@id="carouselExampleIndicators"]/div/div[7]/div[2]/span/div/ul/li[11]/a/label')
        print("Day trips selected")
        cont_btn = d.find_element_by_xpath('//*[@id="id_search_web"]').click()
    except Exception as e:
        print(e)
    finally:
        d.quit()

login2()