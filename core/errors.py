# The output strings should be sufficient intrinsic documentation for each function
# Other methods in the program can call the relevant error from the list below at any time
# This ensures that there is consistency in error reporting to the user, and that errors
# can be added and changed in one place

def word_is_not_valid_input(word: str) -> None:
    print('{} is not a valid input value!'.format(word))

def word_is_not_valid_flag(word: str) -> None:
    print('{} is not a valid flag!'.format(word))

def flag_is_not_initialised(word: str) -> None:
    print('Attempted to use {}, but that flag has not been initialised!'.format(word))

def function_does_not_exist(word: str) -> None:
    print('The function {} does not exist!'.format(word))

def insufficient_arguments() -> None:
    print('Insufficent arguments! Did you supply a loglang file to execute?')

def file_not_found(file_name: str) -> None:
    print('The file {} does not exist!'.format(file_name))

def line_is_not_valid(line: str) -> None:
    print('"{}" is not a valid instruction!'.format(line))

def function_failed_define() -> None:
    print('Failed to define function!')