*** Settings ***
Documentation    To validate the login error message
Resource    training_resource.robot
Library    Collections
Library    ../CustomLibraries/Shop.py
Test Setup      open the browser with OrangeDemo url
Test Teardown   close browser session

*** Variables ***
@{listOfProducts}   Blackberry    Nokia Edge    iphone X


*** Test Cases ***

Verify card display in the shopping page
    fill out the login form    ${user_name}     ${valid_password}
    click the login button
    wait until element is located in the page   ${shop_page_load}
    verify card titles in the shop page
    hello world
    add items to cart and checkout  ${listOfProducts}

*** Keywords ***
Fill out the login form
    [Arguments]     ${username}     ${password}
    input text      id:username  ${username}
    input password  id:password  ${password}

click the login button
    #if ID is used no need to specify the id locator
    click button    id:signInBtn

wait until element is located in the page
    [Arguments]    ${shop_page}
    wait until element is visible    ${shop_page}

verify card titles in the shop page
    @{expectedList} =  CREATE LIST    iphone X    Samsung Note 8    Nokia Edge    Blackberry
    ${elements} =   GET WEBELEMENTS    css:.card-title
    @{actualList} =    CREATE LIST
    FOR    ${element}    IN    @{elements}
        LOG     ${element.text}
        APPEND TO LIST    ${actual_list}    ${element.text}    # APPEND TO LIST is activated by having the Collections library
    END
    LISTS SHOULD BE EQUAL    ${expectedList}   ${actualList}

select the card
    [Arguments]    ${cardName}
    @{elements} =   GET WEBELEMENTS    css:.card-title
    ${index} =    SET VARIABLE    1
    FOR    ${element}    IN    @{elements}
        EXIT FOR LOOP IF    '${cardName}' == '${element.text}'    # When comparing wrap it on a ' qoute
        ${index} =  EVALUATE    ${index} + 1    # When incrementing include the EVALUATE keyword if not robot will not add the value
    END
    CLICK BUTTON    xpath:(//*[@class='card-footer'])[${index}]/button

