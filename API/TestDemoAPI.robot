*** Settings ***
Library    Collections
Library    RequestsLibrary

*** Variables ***
${base_url}    https://rahulshettyacademy.com
${book_id}
${book_name}    RobotFramework

*** Test Cases ***
Play around with dictionary
    # Pag may input need gumawa ng dictionaries
    &{data}    create dictionary    name=rahulshetty    course=${book_name}    website=rahulshettyacademy.com
    log    ${data}
    Dictionary Should Contain Key   ${data}    name
    log    ${data}[name]
    ${url}    get from dictionary    ${data}    website
    log    ${url}

Add book into library database
    # Wrap the payload into a dictionary
    [Tags]    API
    &{req_body}    create dictionary    name=${book_name}    isbn=981466    aisle=324353    author=rahulshetty
    ${response}    POST    ${base_url}/Library/Addbook.php    json=${req_body}    expected_status=200
    log    ${response.json()}
    Dictionary Should Contain Key   ${response.json()}    ID
    ${book_id}    get from dictionary    ${response.json()}    ID
    log    ${book_id}
    set global variable    ${book_id}
    should be equal as strings  successfully added    ${response.json()}[Msg]
    status should be    200    ${response}

Get book into library database
    [Tags]    API
    #GET    url=${base_url}/Library/GetBook.php?ID=${book_id}    expected_status=200
    ${response}    GET    url=${base_url}/Library/GetBook.php    params=ID=${book_id}    expected_status=200
    log    ${response.json()}
    should be equal as strings    ${book_name}    ${response.json()}[0][book_name]
    # [{"book_name":"RobotFramework","isbn":"981466","aisle":"324353","author":"rahulshetty"}]
    status should be    200    ${response}

Delete book into library database
    [Tags]    API
    &{delete_book}    create dictionary    ID=${book_id}
    ${response}    POST    url=${base_url}/Library/DeleteBook.php     json=${delete_book}    expected_status=200
    log    ${response.json()}
    status should be    200    ${response}
    should be equal as strings  book is successfully deleted    ${response.json()}[msg]
