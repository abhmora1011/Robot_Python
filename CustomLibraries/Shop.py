# need to import this
from robot.api.deco import library, keyword

# declare this to include in the library
@library
class Shop:

    #def __init__(self):

#   Method name will be converted to keyword name
    # Declare to include the function to the keyword list
    @keyword
    def hello_world(self):
        print("Hello World!")
