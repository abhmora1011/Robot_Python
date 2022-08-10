from robot.api.deco import library, keyword

from robot.libraries.BuiltIn import BuiltIn

@library
class Activity:
    def __init__(self):
        self.selLib = BuiltIn().get_library_instance("SeleniumLibrary")

    @keyword
    def explicitly_wait(self, time):
        self.selLib.wait_until_element_is_visible("")

