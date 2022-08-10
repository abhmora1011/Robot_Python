# need to import this
from robot.api.deco import library, keyword

# declare this to include in the library
from robot.libraries.BuiltIn import BuiltIn

@library
class Activity:
    def __init__(self):
        #BuiltIn keyword from robot to get the libraries from robot framework
        #self to convert the variable to a global state
        self.selLib = BuiltIn().get_library_instance("SeleniumLibrary")

    def sample_keyword(self):
        print("Hello")

