*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}                      https://qa.letsdochinese.com/KJTCore/resources/index.html
${user_name_txt}            aora
${valid_password_txt}       kjt
${login_btn}                id:login
${username_locator}         id:username
${password_locator}         id:password



*** Keywords ***
fill out the username and password fields
    [Arguments]         ${username}     ${password}
    wait until element is visible    ${username_locator}
    input text          ${username_locator}         ${username}
    input password      ${password_locator}         ${password}

click the login button
    [Arguments]    ${login}
    CLICK BUTTON   ${login}



