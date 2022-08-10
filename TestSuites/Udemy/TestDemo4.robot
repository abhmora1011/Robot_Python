*** Settings ***
Documentation    To validate the login error message
Library    SeleniumLibrary
Library    Collections
Test Template   Verify Unsuccessful Login

# Hindi sya error hindi nya lang mabasa ng tama sa IDE or plugin issue
# Ganito yung mag parametize sa TDD
#*** Test Cases ***      username        password
#Invalid username        dashed          learning
#Invalid password        rahulshetty     plugdhs
#special character       $#@             learning

*** Keywords ***

# This is the test template
Verify Unsuccessful Login
    [Arguments]    ${username}    ${password}
    Open the browser with the Mortgage payment URL
    Fill out the login form    ${username}    ${password}
    wait until it checks and display error message
    verify error message is correct

Open the browser with the Mortgage payment URL
    CREATE WEBDRIVER    Chrome    executable_path=chromedriver
    MAXIMIZE BROWSER WINDOW
    GO TO    https://www.rahulshettyacademy.com/loginpagePractise/

Fill out the login form
    [Arguments]    ${username}    ${password}
    input text      id:username  ${username}
    input password  id:password  ${password}
    CLICK ELEMENT   id:signInBtn

wait until it checks and display error message
    wait until element is visible   css:.alert-danger

verify error message is correct
    element text should be     css:.alert-danger   Incorrect username/password.
    close browser
