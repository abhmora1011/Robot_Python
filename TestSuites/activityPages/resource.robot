*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${res_delivery_btn}         xpath://div[@id='delivery']
${url}                      https://qa.letsdochinese.com/KJTCore/resources/index.html
${browser}                  chrome

*** Keywords ***

open the browser with POS url
        open browser    ${url}      ${browser}
        set browser implicit wait    10 s
        maximize browser window
        SLEEP    3
close browser session
        close browser


