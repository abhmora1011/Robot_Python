*** Settings ***
Documentation    All the page objects and keywords of checkout page
Library    SeleniumLibrary
Resource    Generic.robot

*** Variables ***
${country_location}    //a[text()='India']

*** Keywords ***
Enter the Country and select the terms
    [Arguments]    ${country_name}
    input text    id:country    ${country_name}
    wait until element passed is located on page    //a[text()='${country_name}']
    click element    //a[text()='${country_name}']
    click element    css:.checkbox label

Purchase the Product and Confirm the purchase
    click button    css:.btn-success
    page should contain    Success!
