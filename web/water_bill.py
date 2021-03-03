from selenium import webdriver
from web.views import bill_steps

def run():
    """"""
    steps = bill_steps.BillSteps(webdriver.Chrome(), "waterBill")
    steps.go_to_norwood_start_page()
    steps.go_to_water_bill_page()

    steps.enter_water_bill_account_id()

    steps.assert_water_account_name()
    amount = steps.get_amount_due()
    
    steps.set_amount_due(amount)

    steps.assert_total_is_amount(amount)

    steps.go_to_checkout()

    steps.checkout_as_guest()

    steps.set_address_info()

    steps.toggle_credit_card_radio_button()
    steps.set_payment_info()

    steps.confirm_payment()

    steps.finish()
