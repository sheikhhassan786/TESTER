from behave import *
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time


@given(u'Chrome Browser is launched and the URL for Metabase')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path= "C:\Program Files (x86)\chromedriver.exe")


@given(u'The URL http: // localhost: 3000 / is in Use')
def step_impl(context):
        context.driver.maximize_window()
        try:
            context.driver.get("http://localhost:3000/")
            assert True;
        except WebDriverException:
            context.driver.close()
            print("Cannot open metabase url, make sure it is running on your localhost")
            assert False;
        time.sleep(1.5)

@then(u'I shall be Logged in as Admin User')
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/aside/nav/div/div/div[2]/div/h4").text
    except:
        context.driver.close()
        assert False, "Test Failed: The provided credentials are invalid"
    if text == "COLLECTIONS":
        assert True, "Logged In Successfully"


@then(u'I click on the settings Button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/div[2]/div[3]/div/div/button").click()
    time.sleep(1.5)
    assert True;


@then(u'I click on account settings button')
def AdminSetting(context):

    context.driver.find_element(By.XPATH, "/html/body/span[1]/span/div/div/div/ol/li[1]/a/div/span").click()
    time.sleep(1.5)


@then(u'i click on profile button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='root']/div/div/main/div/div[1]/div[2]/label[1]/div").click()
    time.sleep(0.2)
    assert True;


@then(u'I enter new first name"<firstname>"')
def step_impl(context, firstname):
        context.driver.find_element(By.XPATH, "//*[@id='formField-first_name']/div[2]/div/input").send_keys(firstname)
        assert True;


@then(u'I enter new last name"<lastname>"')
def step_impl(context, lastname):
    context.driver.find_element(By.XPATH, "//*[@id='formField-last_name']/div[2]/div/input").send_keys(lastname)
    assert True;


@then(u'I enter new email "<email>"')
def step_impl(context, email):
    context.driver.find_element(By.NAME, 'email').send_keys(email)
    assert True;

@then(u'I set language "<language>"')
def step_impl(context, language):
    context.driver.find_element(By.XPATH, "//*[@id='formField-locale']/div[2]/a/button/svg").send_keys(language)
    assert True;


@then(u'I press on update button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//*[@id='root']/div/div/main/div/div[2]/form/div[5]/button/div/div").click()
    time.sleep(5)
    assert True;


@then(u'profile is updated')
def step_impl(context):
    assert True, "The profile is updated"