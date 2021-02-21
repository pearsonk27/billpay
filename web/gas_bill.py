from selenium import webdriver
from database import database
from web.views import bill_steps

def run():
    # Cable bill (14th of the month)
    steps = bill_steps.BillSteps(webdriver.Chrome(), "gasBill")

    steps.go_to_gas_bill_page()

    steps.submit_gas_bill_form()

    steps.enter_gas_account_credentials()
    steps.submit_gas_bill_form()

    steps.agree_to_gas_bill_prompt()

    steps.pay_gas_bill_by_credit_card()

    steps.enter_credit_card_info_for_gas_bill()

    steps.make_gas_bill_payment()

    steps.finish()
    