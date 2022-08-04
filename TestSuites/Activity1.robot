*** Settings ***
Documentation       To validate the login error message
Resource            resource.robot
Test Setup          open the browser with POS url
Test Teardown       close browser session


*** Test Cases ***

#Verify if user cannot login using invalid credentials
#    [Documentation]    This is to test if the error message is displayed when user tries to login using invalid credentials
#    ...                 to POS
#    fill out the username and password fields       ${user_name}    ${invalid_password}
#    click the login button
#    verify error login      ${login_error}

Verify if the user send a delivery order
    [Documentation]    This is to test the end to end flow of sending an order to POS
    fill out the username and password fields       ${user_name}    ${valid_password}
    click the login button
    check if main page is visible
    check if the user_lbl is correct
    select restaurant
#    select restaurant
#
#    select an order
#    enter details
#    select category
#    select dish
#    send and verify

*** Keywords ***
fill out the username and password fields
    [Arguments]         ${username}     ${password}
    wait until element is visible    id:username
    input text          id:username         ${username}
    input password      id:password         ${password}

click the login button
    click button        id:login

check if main page is visible
    sleep    3
    wait until element is visible    ${username_lbl}

check if the user_lbl is correct
    element text should be     ${username_lbl}     ${user_name_login}
    sleep    10

select restaurant
    wait until element is visible    id:resdiv
#    wait until element is visible    ${restaurant_btn}
#    click button    ${restaurant_btn}
#    sleep    10

#select an order
#
#enter details
#
#select category
#
#select dish
#
#send and verify
#
#verify error login
#    [Arguments]    ${error}
#    wait until element is visible   ${error}
#    element text should be     ${error}   Username/Password not recognized. Please try again.

