*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${username_lbl}             id:username
${restaurant_btn}           id:6b1bf2af-be65-11e2-97ab-00ff685223c2
${user_name}                aora
${valid_password}           kjt
${invalid_password}         123
${url}                      https://qa.letsdochinese.com/KJTCore/resources/index.html
${login_error}              id:message
${user_name_login}          AORA - TRAINEE

*** Keywords ***
open the browser with POS url
        create webdriver    Chrome  executable_path=chromedriver
        maximize browser window
        Go To       ${url}

close browser session
        close browser


