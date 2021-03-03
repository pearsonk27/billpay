from selenium import webdriver
from web.views import bill_steps

def run():
    # Electric bill (28th of the month)
    # Initiate driver
    steps = bill_steps.BillSteps(webdriver.Chrome(), "electricBill")
    steps.go_to_norwood_start_page()
    steps.go_to_electric_bill_page()

    steps.enter_electric_bill_account_id()

    steps.assert_electric_account_name()
    amount = steps.get_amount_due()
    steps.set_amount_due(amount)
    ## driver.find_element_by_id("ctl00_ctl00_LayoutArea_MainContent_Transaction1_lbtnAddToCart").click()

    steps.go_to_checkout()

    steps.checkout_as_guest()

    steps.set_address_info()

    steps.toggle_credit_card_radio_button()
    steps.set_payment_info()

    steps.confirm_payment()

    steps.finish()
