from selenium import webdriver
from database import database
from web.views import bill_steps

def run():
    """"""
    task_id = database.get_task_id("waterBill")
    execution_log_id = database.start_task(task_id)
    # Initiate driver
    driver = webdriver.Chrome()
    steps = bill_steps.BillSteps(driver, execution_log_id)
    steps.go_to_norwood_start_page()
    steps.go_to_water_bill_page()

    steps.enter_water_bill_account_id()

    steps.assert_water_account_name()
    amount = steps.get_amount_due()
    
    steps.set_amount_due(amount)
    
    steps.assert_total_is_amount(amount)
    
    steps.go_to_checkout()
    
    steps.set_address_info()
    
    steps.toggle_credit_card_radio_button()
    steps.set_payment_info()

    steps.confirm_payment()

    driver.close()
    database.end_task(execution_log_id)
