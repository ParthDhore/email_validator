from selenium import webdriver

def yahoo_check(email):
    driver=webdriver.Chrome('C:/chromedriver.exe')
    driver.get('https://edit.yahoo.com/forgot?stage=fe100')
    driver.find_element('xpath','//*[@id="username"]').send_keys(email)
    driver.find_element('xpath','//*[@id="yid-challenge"]/form/div[2]/button').click()
    try:
        image=driver.find_element('xpath','//*[@id="yid-challenge"]/form/div[2]')
        if image.text=="Sorry, we don't recognize that email address or phone number":
            driver.close()
            return False
        else:
            driver.close()
            return True
    except Exception as e:
        driver.close()
        return True