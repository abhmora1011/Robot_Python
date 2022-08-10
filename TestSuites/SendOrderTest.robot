*** Settings ***
Documentation       To validate the login error message
Resource            activityPages/resource.robot
Resource            activityPages/LoginPage.robot
Resource            activityPages/LandingPage.robot
Library             activityKeywords/Activity.py
Test Setup          open the browser with POS url
Test Teardown       close browser session


*** Test Cases ***

Verify if the user send a delivery order
    [Documentation]    This is to test the end to end flow of sending an order to POS
    fill out the username and password fields       ${user_name_txt}     ${valid_password_txt}
    click the login button          ${login_btn}
    check if main page is visible
    check if the user_lbl is correct
    select restaurant
#    select an order type
#    enter details
#    select category
#    select dish
    #send and verify

*** Keywords ***

select an order type
    click element    ${res_delivery_btn}

enter details
    SLEEP    3
    wait until element is visible   ${phone_txt}
    INPUT TEXT    ${phone_txt}  ${number}
    PRESS KEYS    ${phone_txt}    ENTER
    wait until element is visible   ${street_res}
    INPUT TEXT    ${street_res}   NEW YORK
    PRESS KEYS    ${phone_txt}    ENTER
    PRESS KEYS    ${phone_txt}    ENTER
    wait until element is visible    id:city
    INPUT TEXT    id:city   MEDINA
    PRESS KEYS    id:city    ENTER

    SLEEP    3

select category
    WAIT UNTIL ELEMENT IS ENABLED    css:#cat_6b58fd9b-124f-464c-bafe-1545f31096ff
    Execute JavaScript  $("#cat_6b58fd9b-124f-464c-bafe-1545f31096ff").click()

select dish
    WAIT UNTIL ELEMENT IS ENABLED    css:#dish_a1bf7c71-bd17-49b2-baad-14761074b85b
    Execute JavaScript  $("#dish_a1bf7c71-bd17-49b2-baad-14761074b85b").click()


send and verify
    WAIT UNTIL ELEMENT IS ENABLED   css:#send
    Execute JavaScript  $("#send").click()
    EXECUTE JAVASCRIPT  $("#modalFooterDiv #continueBtn").click()
    EXECUTE JAVASCRIPT  $("#modalFooterDiv #continueBtn").click()

