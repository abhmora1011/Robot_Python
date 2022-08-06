*** Settings ***
Documentation    To validate the login error message
# Library for data driver
Library    DataDriver    file=resources/data.csv    encoding=utf_8    dialect=unix
Library    SeleniumLibrary
Library    Collections
Library    ../CustomLibraries/Shop.py
Test Template   Verify Unsuccessful Login

# Hindi sya error hindi nya lang mabasa ng tama sa IDE or plugin issue
# Ganito yung mag parametize sa TDD
#*** Test Cases ***      username        password
#Invalid username        dashed          learning
#Invalid password        rahulshetty     plugdhs
#special character       $#@             learning

*** Test Cases ***
#    This test case is declare test case since it is mandatory to the robot framework to run.
#    ${username} and ${password} will fetched to the CSV and then it is passed to the keyword implementation
#    abe and ora will populate the username and password if the test case cannot fetch the data from file
#    yung naka declare na login test case dito is mabibigay kung sa CSV is wlaang nakadeclare na test case name
Login with user ${username} and password ${password}    abe    ora

*** Keywords ***

# This is the test template
Verify Unsuccessful Login
#   ${username}    ${password} should be replace the username and password from the testcases row when adding to CSV.
#   see the CSV file for example
#   data in CSV should be separated by comma and not double space
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
    hello world

wait until it checks and display error message
    wait until element is visible   css:.alert-danger

verify error message is correct
    element text should be     css:.alert-danger   Incorrect username/password.
    close browser
