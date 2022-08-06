# need to import this
from robot.api.deco import library, keyword

# declare this to include in the library
from robot.libraries.BuiltIn import BuiltIn


@library
class Shop:

    def __init__(self):
        #BuiltIn keyword from robot to get the libraries from robot framework
        #self to convert the variable to a global state
        self.selLib = BuiltIn().get_library_instance("SeleniumLibrary")

#   Method name will be converted to keyword name
    # Declare to include the function to the keyword list
    @keyword
    def hello_world(self):
        print("Hello World!")

    @keyword
    def add_items_to_cart_and_checkout(self, productList):
        # @{elements} =   GET WEBELEMENTS    css:.card-title
        # GET WEBELEMENTS =  magagamit mo na yung get webelements pero small case and yung space papalitan ng underscore
        self.selLib.get_webelements("css:.card-title")




