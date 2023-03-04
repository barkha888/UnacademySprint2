import time

from behave import *
from hamcrest import assert_that, equal_to
from hamcrest.library import number

from features.pages.LoginPageClass import LoginPageClass


@given("Chrome is opened and Unacademy app is opened")
def step_impl(context):
    pass


@when("User clicks on login button")
def step_impl(context):
    loginpage = LoginPageClass(context.driver)
    loginpage.click_login_icon()
    time.sleep(2)


@step("User enters {}")
def step_impl(context, arg0):
    time.sleep(20)
    mTextbox = LoginPageClass(context.driver)
    mTextbox.enter_mobilenumber_textbox(arg0)
    time.sleep(1)


@step("User again clicks on  login button")
def step_imp(context):
    loginButton = LoginPageClass(context.driver)
    loginButton.click_login_icon2()
    time.sleep(2)


@step("User enter OTP")
def step_impl(context):
   pass


@step("User clicks on Verify otp button")
def step_impl(context):
    time.sleep(10)
    VerifyotpButton = LoginPageClass(context.driver)
    VerifyotpButton.click_verifyotpbutton_button()
    time.sleep(10)


@then("It navigates to Home page")
def step_impl(context):
    time.sleep(2)
    expectTitle = "Unacademy - India's largest learning platform"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectTitle, equal_to(actualTitle))


