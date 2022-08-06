*** Settings ***
Documentation    To validate the login error message
Library    Collections
Library    ../CustomLibraries/Shop.py
Resource    training_resource.robot
Test Setup      open the browser with OrangeDemo url
Test Teardown       close browser session

*** Variables ***
@{listOfProducts}   Blackberry    Nokia Edge


*** Test Cases ***

Verify card display in the shopping page
   # If gusto mo na per test cases lang yung setup and teardown
   # [Setup]    open the browser with OrangeDemo url
   # [Teardown]    close browser session
    fill out the login form    ${user_name}     ${valid_password}
    click the login button
    wait until element is located in the page   ${shop_page_load}
    verify card titles in the shop page
    hello world
    add items to cart and checkout
    select the card    @{listOfProducts}

*** Keywords ***
Fill out the login form
    [Arguments]     ${username}     ${password}
    input text      id:username  ${username}
    input password  id:password  ${password}

click the login button
    #if ID is used no need to specify the id locator
    click button    id:signInBtn

wait login error message
    [Arguments]    ${error}
    wait until element is visible   ${error}
    element text should be     ${error}   Incorrect username/password.

Validate Cards display in the Shopping Page
    Fill out the login form

wait until element is present
    [Arguments]    ${element_link}
    wait until element is visible    ${element_link}

wait until element is located in the page
    [Arguments]    ${shop_page}
    wait until element is visible    ${shop_page}

verify card titles in the shop page
    # use robot keyword to create list
    # @ is used when you create something new list
    # Scalar variable = $   @{variablename}     @{variablename}[0] // A     @{variablename}[1] // B
    # List variable = @     @{variablename}     @{variablename}[0] // A     @{variablename}[1] // B
    # Dictionary variable = &   &{Variablename}     &{Variablename}[key1] // A      &{Variablename}[key2] // B
    @{expectedList} =  CREATE LIST    iphone X    Samsung Note 8    Nokia Edge    Blackberry
    ${elements} =   GET WEBELEMENTS    css:.card-title
    @{actualList} =    CREATE LIST
    FOR    ${element}    IN    @{elements}
        LOG     ${element.text}
        APPEND TO LIST    ${actual_list}    ${element.text}    # APPEND TO LIST is activated by having the Collections library
    END
    LISTS SHOULD BE EQUAL    ${expectedList}   ${actualList}

# To select a specific card
select the card
    [Arguments]    ${cardName}
    @{elements} =   GET WEBELEMENTS    css:.card-title
    ${index} =    SET VARIABLE    1
    FOR    ${element}    IN    @{elements}
        EXIT FOR LOOP IF    '${cardName}' == '${element.text}'    # When comparing wrap it on a ' qoute
        ${index} =  EVALUATE    ${index} + 1    # When incrementing include the EVALUATE keyword if not robot will not add the value
    END
    CLICK BUTTON    xpath:(//*[@class='card-footer'])[${index}]/button

Fill the Login Details and select the user option
    fill out the login form    ${user_name}     ${valid_password}
    click element   css:input[value='user']
    WAIT UNTIL ELEMENT IS VISIBLE    css:.modal-body
    # May issue sa pag click ng alert kaya need mag doble click ng button
    CLICK BUTTON    id:okayBtn
    CLICK BUTTON    id:okayBtnLoginTest2.robot
    WAIT UNTIL ELEMENT IS NOT VISIBLE    css:.modal-body
    #static dropdown keyword    locator     value
    select from list by value    css:select[class='form-control']    teach
    SELECT CHECKBOX    id:terms
    CHECKBOX SHOULD BE SELECTED    id:terms
    SLEEP    3 s


