from selenium.webdriver import Chrome
domain = 'https://generator.email/'

def prepare_driver():
    '''Returns a Firefox Webdriver.'''
    driver = Chrome('/Users/shivendra/Downloads/chromedriver')
    return driver

def gmail_log():
    try:
        driver = prepare_driver()
        driver.get("https://www.gmail.com")
        email_input = driver.find_element_by_name("identifier")
        email_input.send_keys("20495zeba@gmail.com")
        try:
            next_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span")
            next_button.click()
            print("next clicked")
        except Exception as e:
            print ("Error in button click "+str(e))
        driver.implicitly_wait(5)
        try:
            # pass_inp = driver.find_element_by_class_name("rFrNMe A3sRAb YKooDc q9Nsuf zKHdkd sdJrJc").send_keys("zeba20495")
            pass_inp = driver.find_element_by_id("password").send_keys("zeba20495")
        except:
            pass_inp = driver.find_element_by_name("password")
            pass_inp.send_keys("zeba20495")
        sec_button = driver.find_element_by_class_name("CwaK9")
        sec_button.click()
        print("Gmail login complete")
        print(driver.get_cookies())
    except Exception as e1:
        print("Error in login "+str(e1))
    finally:
        if driver:
            driver.quit()
gmail_log()