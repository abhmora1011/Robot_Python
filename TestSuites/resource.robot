*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${username_lbl}             id:username
${restaurant_btn}           css:li[id='8acf750f-b04c-4eba-b9e5-166644f0a89b']
${user_name}                aora
${valid_password}           kjt
${invalid_password}         123
${url}                      https://qa.letsdochinese.com/KJTCore/resources/
${login_error}              id:message
${user_name_login}          AORA - TRAINEE

*** Keywords ***
open the browser with POS url
        create webdriver    Chrome  executable_path=chromedriver
        maximize browser window
        Go To       ${url}

close browser session
        close browser


