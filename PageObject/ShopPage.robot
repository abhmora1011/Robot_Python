*** Settings ***
Documentation    All the page objects and keywords of shop page
Library    SeleniumLibrary
Library    Collections
Resource   Generic.robot

*** Variables ***
${shop_page_load}           css:a.nav-link

*** Keywords ***
wait until element is located in the page
#   [Arguments]    ${shop_page_load}
#   wait until element is visible    ${shop_page}
   wait until element passed is located on page    ${shop_page_load}

verify card titles in the shop page
    @{expectedList} =  CREATE LIST    iphone X    Samsung Note 8    Nokia Edge    Blackberry
    ${elements} =   GET WEBELEMENTS    css:.card-title
    @{actualList} =    CREATE LIST
    FOR    ${element}    IN    @{elements}
        LOG     ${element.text}
        APPEND TO LIST    ${actual_list}    ${element.text}    # APPEND TO LIST is activated by having the Collections library
    END
    LISTS SHOULD BE EQUAL    ${expectedList}   ${actualList}
