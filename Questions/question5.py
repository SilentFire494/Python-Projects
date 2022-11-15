# Define a class which has at least two methods
# get_String: to get a string from console input
# print_String: to print the string in upper case
# Also please include simple test function to test the class methods.
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Enter a string: ")

    def print_string(self):
        print(self.s.upper())


str_obj = InputOutString()
str_obj.get_string()
str_obj.print_string()
