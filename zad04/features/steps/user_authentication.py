from selenium import webdriver
from behave import *

use_step_matcher("re")

@given("the website facebook.com")
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
    context.driver.implicitly_wait(10)
    context.driver.get("https://facebook.com/")

@given("email address (?P<email>.+)")
def step_impl(context, email):
    context.email = email

@given("password (?P<password>.+)")
def step_impl(context, password):
    context.password = password

@when("attempting to log in")
def step_impl(context):
    # context.driver.execute_script("arguments[0].click()", context.driver.find_element(by="id", value="u_0_j_3b"))
    context.url_before = context.driver.current_url
    if context.driver.current_url == "https://www.facebook.com/user_cookie_prompt/":
        context.driver.find_element(by="xpath", value="//div[@aria-label='Allow All Cookies']").click()
    context.driver.find_element(by="id", value="email").send_keys(context.email)
    context.driver.find_element(by="id", value="pass").send_keys(context.password)
    context.driver.find_element(by="xpath", value="//button[@type='submit']").submit()

@then("it fails")
def step_impl(context):
    assert context.driver.current_url != "https://www.facebook.com/?sk=welcome"

@then("user successfuly logs in")
def step_impl(context):
    print(context.driver.current_url)
    print(context.driver.find_elements(by="xpath", value="//input[@aria-label='Search Facebook']")[0].text)
    assert context.driver.current_url == "https://www.facebook.com/?sk=welcome"

