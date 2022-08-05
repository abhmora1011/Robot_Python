*** Settings ***
Documentation    To validate the child window
Library    Collections
Library    String
Resource    training_resource.robot
Test Setup      open the browser with OrangeDemo url
Test Teardown       close browser session

*** Test Cases ***
Validate Child window functionality
    Select the link of the child window
    Verify the user is switched to child window
    Grab the email id in the child window
    Switch to Parent window to enter the email


*** Keywords ***
Select the link of the child window
    CLICK ELEMENT    css:.blinkingText
    SLEEP    5

Verify the user is switched to child window
    SWITCH WINDOW    NEW
    ELEMENT TEXT SHOULD BE    css:h1    DOCUMENTS REQUEST

Grab the email id in the child window
    ${text}     GET TEXT    css:.red
    @{words}    SPLIT STRING   ${text}  at
    # 0 -> Please email us
    # 1 -> mentor@rahulshettyacademy.com with below template to receive response
    ${textSplit}    GET FROM LIST    ${words}   1
    log    ${textSplit}
    @{word_2}    SPLIT STRING   ${textSplit}    with
    ${email}    GET FROM LIST    ${word_2}   0
    SET GLOBAL VARIABLE    ${email}

Switch to Parent window to enter the email
    SWITCH WINDOW    MAIN
    TITLE SHOULD BE    LoginPage Practise | Rahul Shetty Academy
    # don't mind the error it is passed
    INPUT TEXT    id:username    ${email}
    SLEEP   5