*** Settings ***
Documentation    To validate the login error message
Resource    ../../PageObject/Generic.robot
Resource    ../../PageObject/LandingPage.robot
Resource    ../../PageObject/ShopPage.robot
Resource    ../../PageObject/CheckOutPage.robot
Resource    ../../PageObject/ConfirmationPage.robot
Library    Collections
Library    ../../CustomLibraries/Shop.py
Library    AllureReportingLibrary
Suite Setup
Suite Teardown
Test Setup          open the browser with url
Test Teardown       close browser session

*** Variables ***
@{listOfProducts}   Blackberry    Nokia Edge    iphone X
@{country_name}    India

*** Test Cases ***

Verify card display in the shopping page
    [Tags]    Smoke
    # Pwede iconcat yung page name para if ever na may same keyword existing sa ibang page maspecify
    LandingPage.fill out the login form    ${user_name}     ${valid_password}
    click the login button
    #wait until element is located in the page   ${shop_page_load}
    wait until element is located in the page
    verify card titles in the shop page
    add items to cart and checkout  ${listOfProducts}
    CheckOutPage.Verify items in the Checkout Page and Proceed
    ConfirmationPage.Enter the Country and select the terms    @{country_name}
    ConfirmationPage.Purchase the Product and Confirm the purchase
