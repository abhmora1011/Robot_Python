*** Settings ***
Library    SeleniumLibrary
Library    ../activityKeywords/Activity.py

*** Variables ***
${res_delivery_btn}         id:delivery
${number}                   (321) 560-7043
${phone_txt_locator}        id:originPhone
${street_res}               id:address1
${city_txt_locator}         id:city
${cat_btn}                  xpath://div[contains(text(),'CHICKEN')]
${dish_btn}                 id:dish_76172f3b-de16-4052-baba-83dbda0041ed
${send_btn}                 css:#send

*** Keywords ***
select an order type
    click element    ${res_delivery_btn}
    SLEEP    3

enter details
    sample keyword
    wait until element is visible   ${phone_txt_locator}
    INPUT TEXT    ${phone_txt_locator}  ${number}
    PRESS KEYS    ${phone_txt_locator}    ENTER
    PRESS KEYS    ${phone_txt_locator}    ENTER
    wait until element is visible   ${street_res}
    INPUT TEXT    ${street_res}   NEW YORK
    PRESS KEYS    ${phone_txt_locator}    ENTER
    PRESS KEYS    ${phone_txt_locator}    ENTER
    wait until element is visible    ${city_txt_locator}
    INPUT TEXT    ${city_txt_locator}   MEDINA
    PRESS KEYS    ${city_txt_locator}   ENTER
    #EXECUTE JAVASCRIPT    document.body.style.zoom="67%"

select category
    WAIT UNTIL ELEMENT IS ENABLED    ${cat_btn}
    CLICK ELEMENT    ${cat_btn}

select dish
    WAIT UNTIL ELEMENT IS ENABLED    ${dish_btn}
    CLICK ELEMENT    ${dish_btn}
    CLICK ELEMENT    xpath://*[@id="askAndClickModal"]/div/div/div[3]/button
    SLEEP    10

send and verify
    WAIT UNTIL ELEMENT IS ENABLED    ${send_btn}
    CLICK ELEMENT    ${send_btn}
    #Execute JavaScript  $("#send").click()
    EXECUTE JAVASCRIPT  $("#modalFooterDiv #continueBtn").click()
    EXECUTE JAVASCRIPT  $("#modalFooterDiv #continueBtn").click()
