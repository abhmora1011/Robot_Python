*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${Error_Message_Login}      css:.alert-danger
${user_name}                rahulshettyacademy
${valid_password}           learning
${invalid_password}         12345
${url}                      site1
${shop_page_load}           css:a.nav-link

*** Keywords ***
open the browser with OrangeDemo url
        create webdriver    Chrome  executable_path=chromedriver
        maximize browser window
        SET BROWSER IMPLICIT WAIT    10 s
        IF  '${url}' == 'site1'
            ${url}  SET VARIABLE    https://www.rahulshettyacademy.com/loginpagePractise/
        ELSE IF  '${url}' == 'site2'
            ${url}  SET VARIABLE    https://rahulshettyacademy.com
        END

        Go To       ${url}

close browser session
        close browser


