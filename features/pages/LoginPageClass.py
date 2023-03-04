import time

from selenium.webdriver.common.by import By

class LoginPageClass:

    def __init__(self,driver):
        self.driver=driver
        # Element Locator Values

        self.loginButtonElement = "//*[text()= 'Log in']"
        self.mobileNumberElement = "//input[@placeholder='Enter your mobile number']"
        self.loginButton2Element = "//button[@color='green' and @aria-label='Login']"
        self.OTPTextBoxElement = "//input[@placeholder='One time password']"
        self.VerifyOTPTextBoxElement = "//button[@color='green' and @aria-label='Verify OTP']"

        # Creating Element Methods

    def click_login_icon(self):
        loginbutton = self.driver.find_element(By.XPATH, self.loginButtonElement)
        loginbutton.click()

    def enter_mobilenumber_textbox(self, mn):
        mobilenumberTextBox = self.driver.find_element(By.XPATH, self.mobileNumberElement)
        mobilenumberTextBox.send_keys(mn)

    def click_login_icon2(self):
        loginbutton = self.driver.find_element(By.XPATH, self.loginButton2Element)
        loginbutton.click()



    def click_verifyotpbutton_button(self):
        VerifyOTPButton = self.driver.find_element(By.XPATH, self.VerifyOTPTextBoxElement)
        time.sleep(20)
        VerifyOTPButton.click()
        time.sleep(25)




