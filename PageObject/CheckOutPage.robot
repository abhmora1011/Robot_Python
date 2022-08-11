*** Settings ***
Documentation    All the page objects and keywords of checkout page
Library    SeleniumLibrary

*** Keywords ***
Verify items in the Checkout Page and Proceed
    click element    css:.btn-success