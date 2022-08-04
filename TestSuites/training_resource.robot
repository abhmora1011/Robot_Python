*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${Error_Message_Login}      css:.alert-danger
${user_name}                rahulshettyacademy
${valid_password}           learning
${invalid_password}         12345
${url}                      https://www.rahulshettyacademy.com/loginpagePractise/
${element}                  css:a.nav-link
${shop_page_load}           css:a.nav-link

*** Keywords ***
open the browser with OrangeDemo url
        create webdriver    Chrome  executable_path=chromedriver
        maximize browser window
        Go To       ${url}

close browser session
        close browser


