# This will open a web browser, sign into venmo, and pay someone some money

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
# import SendKeys
import time
import venmo_info
import datetime
import os

VENMO_URL = 'https://venmo.com/'

browser = webdriver.Chrome()
browser.get(VENMO_URL)

def make_pay_request(amount, description):

    if os.path.isfile('cookies.pkl'):
        # there is a cookie file

        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            browser.add_cookie(cookie)

        # click on the sign in link
        signin_link = browser.find_element_by_link_text("Sign In")
        signin_link.click()

        # enter the email and password and send it
        username_box = browser.find_element_by_name("phoneEmailUsername")
        username_box.send_keys(venmo_info.my_u)
        password_box = browser.find_element_by_name("password")
        password_box.send_keys(venmo_info.my_p)
        send_button = browser.find_element_by_link_text("Sign In")
        send_button.click()

        # enter the person's name you want to pay
        time.sleep(5)
        name_box = browser.find_element_by_class_name("onebox_prefill")
        name_box.click()
        name_text_box = browser.find_element_by_class_name("paddingUnifier")
        name_text_box.send_keys(venmo_info.payee_name)
        name_text_box.send_keys(Keys.ENTER)
        payment_box = browser.find_element_by_class_name("mainTextBox")
        time.sleep(1)
        payment_box.click()
        # SendKeys.SendKeys(amount + description, with_spaces=True)
        # click the pay button
        pay_button = browser.find_element_by_id("onebox_pay_toggle")
        pay_button.click()
        name_text_box = browser.find_element_by_class_name("paddingUnifier")
        name_text_box.send_keys(venmo_info.payee_name)

        # click the send button
        send_button = browser.find_element_by_id("onebox_send_button")
        send_button.click()

    else:
        # click on the sign in link
        signin_link = browser.find_element_by_link_text("Sign In")
        signin_link.click()
        print("Couldn't find the cookie file, you will need two factor authorization and then cookie will be saved")
        # wait a while until the user fully signs in
        time.sleep(60)
        # Save the cookies
        pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))

    time.sleep(10)
    browser.close()

make_pay_request(45.00, "Electric Bill for May")