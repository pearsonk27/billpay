from web.views import bill_view_config, my_info
from step_logging import step_logging
from selenium.webdriver.common.keys import Keys
from database import database
import time
import re

@step_logging.decorate_all_functions(step_logging.log_on_call)
class BillSteps:

    def __init__(self, driver, task_name):
        """Initialize BillSteps Class"""
        self.driver = driver
        self.task_name = task_name
        self.task_id = database.get_task_id(task_name)
        self.execution_log_id = database.start_task(self.task_id)

    def go_to_norwood_start_page(self):
        """Go to Norwood Start Page"""
        self.driver.get((bill_view_config.StartPage.norwood_bill_pay_start_page()))
        time.sleep(3)

    def go_to_cable_bill_page(self):
        """Go to Norwood Cable Bill Page"""
        self.driver.find_element_by_xpath(bill_view_config.StartPage.cable_bill_link()).click()
        time.sleep(3)

    def go_to_electric_bill_page(self):
        """Go to Norwood Electric Bill Page"""
        self.driver.find_element_by_xpath(bill_view_config.StartPage.electric_bill_link()).click()
        time.sleep(3)
    
    def go_to_water_bill_page(self):
        """Go to Norwood Water Bill Page"""
        self.driver.find_element_by_xpath(bill_view_config.StartPage.water_bill_link()).click()
        time.sleep(3)

    def go_to_gas_bill_page(self):
        """Go to National Grid Bill Pay Page"""
        self.driver.get(bill_view_config.GasBill.nation_grid_bill_pay_page())
        time.sleep(3)

    def submit_gas_bill_form(self):
        """Submit gas bill form"""
        self.driver.find_element_by_name("SUBMIT").click()
        time.sleep(3)

    def enter_gas_account_credentials(self):
        """Enter gas account crdentials"""
        self.driver.find_element_by_name("LOGIN").send_keys(my_info.gas_login())
        self.driver.find_element_by_name("PASSWORD").send_keys(my_info.gas_password())

    def agree_to_gas_bill_prompt(self):
        """Agree to gas bill prompt"""
        self.driver.find_element_by_name("AGREE").click()
        time.sleep(3)

    def pay_gas_bill_by_credit_card(self):
        """Go to page for gas bill credit card payment"""
        self.driver.get("https://paynow7.speedpay.com/NationalGrid/PayByCreditCard.asp")
        time.sleep(3)

    def enter_credit_card_info_for_gas_bill(self):
        """Enter credit card info for gas bill"""
        self.driver.find_element_by_name("DEBIT_ACCOUNT").send_keys(my_info.credit_card_number())
        self.driver.find_element_by_xpath(bill_view_config.GasBill.credit_card_expiration_month_selector(my_info.credit_card_expriation_month_number_and_name())).click()
        self.driver.find_element_by_xpath(bill_view_config.GasBill.credit_card_exiration_month_selector(my_info.credit_card_expiration_year())).click()
        self.driver.find_element_by_name("CVV").send_keys(my_info.credit_card_cvv())
        self.driver.find_element_by_name("Continue").click()
        time.sleep(3)
        
    def enter_account_id(self):
        """Enter Norwood Cable Account ID"""
        elem = self.driver.find_element_by_name(bill_view_config.CableBill.cable_account_id_text_box())
        elem.clear()
        elem.send_keys(my_info.cable_account_number())
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

    def enter_electric_bill_account_id(self):
        """Enter Norwood Electric Account ID"""
        self.driver.find_element_by_name("ctl00$ctl00$LayoutArea$MainContent$Transaction1$tblI2646").send_keys("1810131335")
        self.driver.find_element_by_id("ctl00_ctl00_LayoutArea_MainContent_Transaction1_lbtnContinue").click()
        time.sleep(3)

    def enter_water_bill_account_id(self):
        """Enter Norwood Water Account ID"""
        self.driver.find_element_by_name("ctl00$ctl00$LayoutArea$MainContent$Transaction1$tblI2651").send_keys("11410128392")
        self.driver.find_element_by_id("ctl00_ctl00_LayoutArea_MainContent_Transaction1_lbtnContinue").click()
        time.sleep(3)

    def assert_name(self):
        """Enter Assert Name value"""
        elem2 = self.driver.find_element_by_name(bill_view_config.CableBill.name_text_box())
        assert elem2.get_attribute("value") == my_info.my_name_first_last()

    def assert_electric_account_name(self):
        """Assert correct account name"""
        assert self.driver.find_element_by_name("ctl00$ctl00$LayoutArea$MainContent$Transaction1$tbifI2649").get_attribute("value") == "KRISTOFER PEARSON"

    def assert_water_account_name(self):
        """Assert Water Account Name"""
        assert self.driver.find_element_by_name("ctl00$ctl00$LayoutArea$MainContent$Transaction1$tbifI2654").get_attribute("value") == "KRISTOFER PEARSON"

    def get_amount_due(self):
        """Get amount due"""
        elem3 = self.driver.find_element_by_id(bill_view_config.CommonBill.amount_due_text())
        amount = re.search(r"\d.*", elem3.text).group()
        return amount

    def set_amount_due(self, amount):
        """Set amount due"""
        elem4 = self.driver.find_element_by_name(bill_view_config.CommonBill.amount_text_box())
        elem4.clear()
        elem4.send_keys(amount)
        elem4.send_keys(Keys.RETURN)
        time.sleep(3)

    def assert_total_is_amount(self, amount):
        """Assert total is expected amount"""
        elem5 = self.driver.find_element_by_css_selector(bill_view_config.CableBill.total_css_selector())
        total = re.search(r"\d.*", elem5.text).group()
        assert total == amount

    def go_to_checkout(self):
        """Click Checkout Button"""
        self.driver.find_element_by_name(bill_view_config.CommonBill.checkout_button()).click()
        time.sleep(3)

    def checkout_as_guest(self):
        """Click checkout as guest button"""
        self.driver.find_element_by_name(bill_view_config.CommonBill.check_out_as_guest_button()).click()
        time.sleep(3)

    def set_address_info(self):
        """Set Address Info"""
        elem6 = self.driver.find_element_by_name(bill_view_config.CommonBill.address_line1_text_box())
        elem6.clear()
        elem6.send_keys(my_info.address_line_1())
        self.driver.find_element_by_name(bill_view_config.CommonBill.address_line2_text_box()).send_keys(my_info.address_line_2())
        self.driver.find_element_by_name(bill_view_config.CommonBill.city_text_box()).send_keys(my_info.city())
        self.driver.find_element_by_xpath(bill_view_config.CommonBill.state_dropdown(my_info.state())).click()
        self.driver.find_element_by_name(bill_view_config.CommonBill.zip_code_text_box()).send_keys(my_info.zip_code())
        self.driver.find_element_by_name(bill_view_config.CommonBill.phone_number_text_box()).send_keys(my_info.phone_number())
        self.driver.find_element_by_name(bill_view_config.CommonBill.email_text_box()).send_keys(my_info.email())
        # driver.execute_script("javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$LayoutArea$MainContent$BillingInfo1$btnProceed&quot;, &quot;&quot;, true, &quot;BillingAddress&quot;, &quot;&quot;, false, false))")
        self.driver.find_element_by_name(bill_view_config.CommonBill.proceed_button()).click()
        time.sleep(3)

    def toggle_credit_card_radio_button(self):
        """Toggle credit card radio button"""
        self.driver.find_element_by_css_selector(bill_view_config.CommonBill.credit_card_radio_button()).click()
        time.sleep(3)

    def set_payment_info(self):
        """Set payment info"""
        self.driver.find_element_by_name(bill_view_config.CommonBill.card_holder_name_text_box()).send_keys(my_info.card_holder_name())
        self.driver.find_element_by_name(bill_view_config.CommonBill.credit_card_number_text_box()).send_keys(my_info.credit_card_number())
        self.driver.find_element_by_xpath(bill_view_config.CommonBill.credit_card_expiration_date_month_dropdown(my_info.credit_card_expiration_month())).click()
        self.driver.find_element_by_xpath(bill_view_config.CommonBill.credit_card_expiration_year_dropdown(my_info.credit_card_expiration_year())).click()
        self.driver.find_element_by_name(bill_view_config.CommonBill.credit_card_cvv()).send_keys(my_info.credit_card_cvv())
        self.driver.find_element_by_id(bill_view_config.CommonBill.payment_proceed_button()).click()
        time.sleep(3)

    def confirm_payment(self):
        """Confirm Payment"""
        # self.driver.execute_script(bill_view_config.CommonBill.show_confirmation_dialog_script())
        self.driver.find_element_by_id(bill_view_config.CommonBill.submit_payment_button()).click()
        time.sleep(3)
        self.driver.find_element_by_id(bill_view_config.CommonBill.confirm_payment_button()).click()
        time.sleep(10)

    def make_gas_bill_payment(self):
        """Make gas bill payment"""
        self.driver.find_element_by_name("MakePayment").click()
        time.sleep(3)

    def finish(self):
        """End task"""
        self.driver.close()
        database.end_task(self.execution_log_id)
