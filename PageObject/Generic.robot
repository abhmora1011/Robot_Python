*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    site1

*** Keywords ***
open the browser with url
        create webdriver    Chrome  executable_path=chromedriver
        delete all cookies
        maximize browser window

        SET BROWSER IMPLICIT WAIT    10 s
        IF  '${url}' == 'site1'
            ${url}  SET VARIABLE    https://www.rahulshettyacademy.com/loginpagePractise/
        ELSE IF  '${url}' == 'site2'
            ${url}  SET VARIABLE    https://rahulshettyacademy.com
        END

        Go To       ${url}

#open the browser with url
#        [Arguments]    ${browser_name}
#        create webdriver    ${browser_name}  executable_path=${browser_name}
#        Go To       ${url}

close browser session
        close browser

# Para maging reusable sya sa ibang pages na gagamit ng wait element
wait until element passed is located on page
    [Arguments]    ${page_locator}
    wait until element is visible    ${page_locator}


