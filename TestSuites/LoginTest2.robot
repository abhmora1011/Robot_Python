*** Settings ***
Documentation    To validate the login error message
Library    Collections
Resource    training_resource.robot
Test Setup      open the browser with OrangeDemo url
Test Teardown       close browser session

*** Test Cases ***
#Verify that error message appears
#    [Documentation]    Verify the flow until the error message show
#    Fill out the login form    ${user_name}     ${invalid_password}
#    click the login button
#    wait login error message    ${Error_Message_Login}
#
#Verify end to end process
#    [Documentation]    Verify the flow of end to end process
#    fill out the login form    ${user_name}     ${valid_password}
#    click the login button
#    wait until element is present       ${element}

Verify card display in the shopping page
    fill out the login form    ${user_name}     ${valid_password}
    click the login button
    wait until element is located in the page   ${shop_page_load}
    verify card titles in the shop page


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
    #use robot keyword to create list
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

select the card
    [Arguments]    ${cardName}

    click button    xpath:(//*[@class='card-footer'])[4]/button