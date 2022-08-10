*** Settings ***
Library    SeleniumLibrary

*** Variables ***


${res_delivery_btn}         xpath://div[@id='delivery']
${url}                      https://qa.letsdochinese.com/KJTCore/resources/index.html

${number}                   (321) 560-7043
${phone_txt}                id:originPhone
${street_res}               xpath://*[@id="address1"]

*** Keywords ***
open the browser with POS url
        create webdriver    Chrome  executable_path=chromedriver
        set browser implicit wait    10 s
        maximize browser window
        EXECUTE JAVASCRIPT    document.body.style.zoom="80%"
        Go To       ${url}

close browser session
        close browser


