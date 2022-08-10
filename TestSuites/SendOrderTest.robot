*** Settings ***
Documentation       To validate the login error message
Resource            activityPages/resource.robot
Resource            activityPages/LoginPage.robot
Resource            activityPages/LandingPage.robot
Resource            activityPages/OrderingPage.robot
Library             DataDriver    file=activityData/activity.csv    encoding=utf_8    dialect=unix
Test Setup          open the browser with POS url
Test Teardown       close browser session
Test Template       Verify if the user send a delivery order

*** Test Cases ***

End to end test using valid ${username} and ${password}    aora    ora

*** Keywords ***

Verify if the user send a delivery order
    [Tags]    Smoke
    [Documentation]    This is to test the end to end flow of sending an order to POS
    fill out the username and password fields       ${user_name_txt}     ${valid_password_txt}
    click the login button          ${login_btn}
    check if main page is visible
    check if the user_lbl is correct
    select restaurant
    select an order type
    enter details
    select category
    select dish
    send and verify





