*** Settings ***
Documentation    To validate the login error message
Library     SeleniumLibrary

*** Variables ***
${Error_Message_Login}  css:.alert-danger

*** Test Cases ***
Verify that login works
    open the browser with OrangeDemo url
    fill out the username and password fields
    wait login error message
    verify error message is correct

*** Keywords ***
open the browser with OrangeDemo url
    create webdriver      Chrome  executable_path=../chromedriver
    maximize browser window
    Go To   https://www.rahulshettyacademy.com/loginpagePractise/

fill out the username and password fields
    input text    id:username  rahulshettyacademy
    input password  id:password  admin1234
    #if ID is used no need to specify the id locator
    click button    signInBtn

wait login error message
    wait until element is visible   ${Error_Message_Login}

verify error message is correct
    #${result}   get text    ${Error_Message_Login}
    #should be equal as strings   ${result}   Incorrect username/password.
    element text should be     ${Error_Message_Login}   Incorrect username/password.
    close browser