
class StartPage:

    def norwood_bill_pay_start_page():
        return "https://unipaygold.unibank.com/transactioninfo.aspx?customerid=444"

    def national_grid_start_page():
        return "https://paynow7.speedpay.com/NationalGrid/index.asp"

    def cable_bill_link():
        return "//li/a[text()='Cable']"

    def electric_bill_link():
        return "//li/a[text()='Light']"

    def water_bill_link():
        return "//li/a[text()='Water']"


class CableBill:

    def cable_account_id_text_box():
        return "ctl00$ctl00$LayoutArea$MainContent$Transaction1$tblI2656"

    def name_text_box():
        return "ctl00$ctl00$LayoutArea$MainContent$Transaction1$tbifI2659"

    def total_css_selector():
        return ".large-6.large-offset-4.columns.total"


class ElectricBill:

    def name_text_box():
        return "ctl00$ctl00$LayoutArea$MainContent$Transaction1$tbifI2649"


class GasBill:

    def nation_grid_bill_pay_page():
        return "https://paynow7.speedpay.com/NationalGrid/index.asp"

    def credit_card_expiration_month_selector(month_number_and_name):
        return f"//select[@name='Month']/option[text()='{month_number_and_name}']"

    def credit_card_exiration_month_selector(year):
        return f"//select[@name='Year']/option[text()='{year}']"


class CommonBill:

    def amount_due_text():
        return "ctl00_ctl00_LayoutArea_MainContent_Transaction1_lblAmountDue"

    def amount_text_box():
        return "ctl00$ctl00$LayoutArea$MainContent$Transaction1$AmtTextBox"

    def checkout_button():
        return "ctl00$ctl00$LayoutArea$MainContent$Cart1$rptCart$ctl02$btnCheckout"

    def address_line1_text_box():
        return "ctl00$ctl00$LayoutArea$MainContent$BillingInfo1$tbAddress1"

    def address_line2_text_box():
        return "ctl00$ctl00$LayoutArea$MainContent$BillingInfo1$tbAddress2"

    def city_text_box():
        return "ctl00$ctl00$LayoutArea$MainContent$BillingInfo1$tbCity"

    def state_dropdown(state):
        return f"//select[@name='ctl00$ctl00$LayoutArea$MainContent$BillingInfo1$ddlState']/option[text()='{state}']"

    def zip_code_text_box():
        return "ctl00$ctl00$LayoutArea$MainContent$BillingInfo1$tbZipCode"

    def phone_number_text_box():
        return "ctl00$ctl00$LayoutArea$MainContent$BillingInfo1$tbPhoneNo"

    def email_text_box():
        return "ctl00$ctl00$LayoutArea$MainContent$BillingInfo1$tbEmail"

    def proceed_button():
        return "ctl00$ctl00$LayoutArea$MainContent$BillingInfo1$btnProceed"

    def credit_card_radio_button():
        return "input[type='radio'][value='rdbtnCreditCard']"

    def card_holder_name_text_box():
        return "ctl00$ctl00$LayoutArea$MainContent$Paymethod1$tbCardholderName"

    def credit_card_number_text_box():
        return "ctl00$ctl00$LayoutArea$MainContent$Paymethod1$tbCreditCardNo"

    def credit_card_expiration_date_month_dropdown(month):
        return f"//select[@name='ctl00$ctl00$LayoutArea$MainContent$Paymethod1$drpMonthList']/option[text()='{month}']"

    def credit_card_expiration_year_dropdown(year):
        return f"//select[@name='ctl00$ctl00$LayoutArea$MainContent$Paymethod1$drpYeartList']/option[text()='{year}']"

    def credit_card_cvv():
        return "ctl00$ctl00$LayoutArea$MainContent$Paymethod1$tbCVV2"

    def payment_proceed_button():
        return "ctl00$ctl00$LayoutArea$MainContent$Paymethod1$btnProceed"

    def show_confirmation_dialog_script():
        return "var dlg = $('#confirmPaymentModal').foundation('reveal','open',{css:{open:{'opacity':0,'visibility':'visible','display':'block'}}});dlg.appendTo(jQuery('form:first'));return false;"

    def confirmation_dialog_proceed_button():
        return "ctl00$ctl00$LayoutArea$MainContent$Confirmation1$btnProceed"

    def check_out_as_guest_button():
        return "ctl00$ctl00$LayoutArea$MainContent$SignIn1$btnCheckOutGuest"

    def submit_payment_button():
        return "confirmPayment_modal"

    def confirm_payment_button():
        return "ctl00_ctl00_LayoutArea_MainContent_Confirmation1_btnModalSubmit"
