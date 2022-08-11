*** Settings ***
Documentation    All the page objects and keywords of landing page
Library    SeleniumLibrary

*** Variables ***
${Error_Message_Login}      css:.alert-danger
${user_name}                rahulshettyacademy
${valid_password}           learning
${invalid_password}         12345

*** Keywords ***
Fill out the login form
    [Arguments]     ${username}     ${password}
    input text      id:username  ${username}
    input password  id:password  ${password}

click the login button
    click button    id:signInBtn