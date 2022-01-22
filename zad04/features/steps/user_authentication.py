import time
import unittest
from selenium import webdriver
from behave import *

use_step_matcher("re")

@given("the website wp.pl")
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.wp.pl/")

@given("email address (?P<email>.+)")
def step_impl(context, email):
    context.email = email

@given("password (?P<password>.+)")
def step_impl(context, password):
    context.password = password

@when("attempting to log in")
def step_impl(context):
    context.driver.execute_script("arguments[0].click()", context.driver.find_element(by="id", value="ol-widget-login-button"))
    context.url_before = context.driver.current_url
    context.driver.find_element(by="id", value="login").send_keys(context.email)
    context.driver.find_element(by="id", value="password").send_keys(context.password)
    context.driver.find_element(by="xpath", value="//button[@type='submit']").submit()

@then("it fails")
def step_impl(context):
    assert len(context.driver.find_elements(by="xpath", value="//div[@data-testid='login-error']")) != 0
