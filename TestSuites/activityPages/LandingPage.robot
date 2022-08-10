*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${username_lbl}             id:username
${user_name_login}          AORA - TRAINEE - MNL
${restaurant_btn}           xpath://*[@id="6b1bf2af-be65-11e2-97ab-00ff685223c2"]

*** Keywords ***

check if main page is visible
    sleep    3
    wait until element is visible    ${username_lbl}    10s

check if the user_lbl is correct
    element text should be     ${username_lbl}     ${user_name_login}

select restaurant
    wait until element is visible    ${restaurant_btn}
    click element    ${restaurant_btn}