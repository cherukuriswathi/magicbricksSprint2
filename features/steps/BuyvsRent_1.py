from behave import *
from hamcrest import equal_to, assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.pages.BuyvsRentClass_1 import BuyvsRentClass_1

@given("Chrome is opened and  MagicBricks application is opened")
def step_impl(context):
    context.driver.implicitly_wait(3)
@when(u'User navigates to MagicBricks landing page')
def step_impl(context):
    context.driver.implicitly_wait(3)
    expectedTitle = "Real Estate | Property in India | Buy/Sale/Rent Properties | MagicBricks"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert expectedTitle == actualTitle
    context.driver.implicitly_wait(5)
@step(u'Hover the mouse on MB Advice and Click on buy v/s rent link')
def step_impl(context):
    mbadvice= BuyvsRentClass_1(context.driver)
    mbadvice.mouse_hover()
    buyrent=BuyvsRentClass_1(context.driver)
    buyrent.buy_rent_click()
    context.driver.implicitly_wait(5)

@Then(u'User navigates to the Buy vs Rent Landing page')
def step_impl(context):
    context.driver.implicitly_wait(5)
    expectedTitle = "Know whether to Buy or Rent your Property | Buy Vs Rent Calculator | Magicbricks Advice"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert expectedTitle == actualTitle
    context.driver.implicitly_wait(4)
#--------------------------------------------------------------------------------------------------------------
@then("Click on Tax Button")
def step_impl(context):
    taxbutton= BuyvsRentClass_1(context.driver)
    taxbutton.Tax_Button()
    context.driver.implicitly_wait(10)
@then('Drag and set the value of Down payment')
def step_impl(context):
    context.driver.implicitly_wait(10)
    dragger= BuyvsRentClass_1(context.driver)
    dragger.dragger_click()
    context.driver.implicitly_wait(10)
    radiobutton=BuyvsRentClass_1(context.driver)
    radiobutton.dragger_click()
#---------------------------------------------------------------------------------------------------------

@then("User Hover the mouse on My Activity and click on login Button")
def step_impl(context):
    myActivity = BuyvsRentClass_1(context.driver)
    myActivity.Hover_to_Myactivity()
    context.driver.implicitly_wait(10)
    Login=BuyvsRentClass_1(context.driver)
    Login.Login_Click()
    context.driver.implicitly_wait(10)

@then("User is not able to login from this page")
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = "SERVER - Error report"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert expectedTitle == actualTitle

#---------------------------------------------------------------------------------------------------------------------------------
@step("User clicks on Property button")
def step_impl(context):
    propertyButton = BuyvsRentClass_1(context.driver)
    propertyButton.Property_Button()
    context.driver.implicitly_wait(10)

@then("Click on the Click Here if>1lac link")
def step_impl(context):
    Link=BuyvsRentClass_1(context.driver)
    Link.Property_Button()
    context.driver.implicitly_wait(10)

@then("Enter the value from the dropdown")
def step_impl(context):
    dropdown = context.driver.find_element(By.XPATH, "//*[@id='buyVsRentCalcSection']/div/div[1]/div[2]/div[1]/div[2]/div[6]/div[4]/div[1]/div/div/select")
    dropdownOption = Select(dropdown)
    print(dropdownOption.first_selected_option.text)
    context.driver.implicitly_wait(3)
    dropdownOption.select_by_visible_text("10 Lac")
    value = context.driver.find_element(By.XPATH, "//*[@id='currentRateLacDisplay']/option[11]")
    print("Is element selected --> ", value.is_selected())
    print("Text of value is --> " + value.text)
    context.driver.implicitly_wait(5)

    dropdown = context.driver.find_element(By.XPATH,"//*[@id='buyVsRentCalcSection']/div/div[1]/div[2]/div[1]/div[2]/div[6]/div[4]/div[2]/div/div/select")
    dropdownOption = Select(dropdown)
    print(dropdownOption.first_selected_option.text)
    context.driver.implicitly_wait(3)
    dropdownOption.select_by_visible_text("50,000")
    value = context.driver.find_element(By.XPATH, "//*[@id='currentRateThousandDisplay']/option[6]")
    print("Is element selected --> ", value.is_selected())
    print("Text of value is --> " + value.text)
    context.driver.implicitly_wait(5)
#--------------------------------------------------------------------------------------------------------------------------
@then("Click on Advice link")
def step_impl(context):
    adviceLink=BuyvsRentClass_1(context.driver)
    adviceLink.AdviceLink_click()

@step("User will be navigated to property advice page")
def step_impl(context):
    context.driver.implicitly_wait(3)
    expectedTitle = "Property Advice | Real Estate Expert Advice For Home Buyers | MagicBricks"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert expectedTitle == actualTitle
    context.driver.implicitly_wait(5)


#----------------------------------------------------------------------------------------------------------------------------

@then("Click on Home Link")
def step_impl(context):
    Homelink=BuyvsRentClass_1(context.driver)
    Homelink.Home_link()


@step("User will be redirected to the home page of the application")
def step_impl(context):
    expectedTitle = "Real Estate | Property in India | Buy/Sale/Rent Properties | MagicBricks"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert expectedTitle == actualTitle
    context.driver.implicitly_wait(10)