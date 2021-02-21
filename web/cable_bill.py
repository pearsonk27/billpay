from selenium import webdriver
from database import database
from web.views import bill_steps

def run():
    """"""
    task_id = database.get_task_id("cableBill")
    execution_log_id = database.start_task(task_id)
    # Cable bill (14th of the month)
    # Initiate driver
    driver = webdriver.Chrome()
    steps = bill_steps.BillSteps(driver, execution_log_id)
    steps.go_to_norwood_start_page()
    # driver.get("https://unipaygold.unibank.com/transactioninfo.aspx?customerid=444")
    # Given website setup, you cannot get to the right link without starting the session with norwood id (444)
    # Link to cable bill is done with javascript postback
    steps.go_to_cable_bill_page()
    # Enter Account Number
    steps.enter_account_id()
    # Assert you have the right account
    steps.assert_name()
    # Get amount due
    amount = steps.get_amount_due()
    # Type amount in Pay Amount
    steps.set_amount_due(amount)
    # Assert that the total amount is the a`mount you have in memory
    steps.assert_total_is_amount(amount)
    # Submit form
    # driver.execute_script("javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$LayoutArea$MainContent$Cart1$rptCart$ctl02$btnCheckout&quot;, &quot;&quot;, true, &quot;&quot;, &quot;&quot;, false, false))")
    steps.go_to_checkout()
    # Set a lot of things (need multi set method)
    steps.set_address_info()
    # Next page is credit card info
    steps.toggle_credit_card_radio_button()
    steps.set_payment_info()

    steps.confirm_payment()

    driver.close()
    database.end_task(execution_log_id)