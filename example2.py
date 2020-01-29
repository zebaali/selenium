from selenium.webdriver import Chrome
domain = 'https://generator.email/'
#from selenium.webdriver.support.select import Select

def prepare_driver():
    '''Returns a Chrome Webdriver.'''
    driver = Chrome('/Users/shivendra/Downloads/chromedriver')
    return driver

try:
    driver = prepare_driver()
    driver.get("https://www.gmail.com/")
    #import pdb;pdb.set_trace()
    print(driver.get_cookies())
#    dd = Select(driver.select_by_visible_text('Management'))
 #   dd.select_by_value()
except Exception as e:
    print("Error" + str(e))

driver.quit()