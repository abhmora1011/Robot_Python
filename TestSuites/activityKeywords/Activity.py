from robot.api.deco import library, keyword

from robot.libraries.BuiltIn import BuiltIn

@library
class Activity:
    def __init__(self):
        self.selLib = BuiltIn().get_library_instance("SeleniumLibrary")

    @keyword
    def sample_keyword(self):
        print("Hello")

