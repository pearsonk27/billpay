import time
from database import database
from web.views import bill_view_config
from selenium import webdriver
from web.views.bill_steps import BillSteps
from messaging import email

def run():
    task_id = database.get_task_id("test")
    execution_log_id = database.start_task(task_id)

    execution_step_log_id = database.start_execution_step(execution_log_id, "Test step 1")
    time.sleep(10)
    database.end_execution_step(execution_step_log_id)

    execution_step_log_id = database.start_execution_step(execution_log_id, "Test step 2")
    time.sleep(10)
    database.end_execution_step(execution_step_log_id)

    execution_step_log_id = database.start_execution_step(execution_log_id, "Test step 3")
    time.sleep(10)
    database.end_execution_step(execution_step_log_id)

    database.end_task(execution_log_id)

def run2():
    print(bill_view_config.StartPage.norwood_bill_pay_start_page())

def run3():
    task_id = database.get_task_id("bogus")
    
    print(task_id)

def run4():
    task_id = database.get_task_id("test")
    execution_log_id = database.start_task(task_id)

    driver = webdriver.Chrome()
    bill_steps = BillSteps(driver, execution_log_id)
    bill_steps.go_to_norwood_start_page()
    time.sleep(10)

    driver.close()
    database.end_task(execution_log_id)

def run5():
    email.send_failure_message("test", "test_step", "test failure message")

def run6():
    bill_steps = BillSteps(None, "test")
    bill_steps.test_throw_exception()
    print("We should not get here")
