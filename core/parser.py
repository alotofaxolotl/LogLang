import core.errors as errors
import core.data as data


# PARSER functions take raw input data and make it more meaningful
# for the program


# Recognised symbols in the language
symbols = {
    'comment': '//',
    'function_declaration': '$',
    'into': '->'
}

# If the line starts with the comment symbol, return True
# otherwise, return false
def is_line_comment(line: str) -> bool:

    return line.startswith(symbols['comment'])


# If the line starts with the function declaration symbol, return True
# otherwise, return false
def is_line_function_declaration(line: str) -> bool:

    return line.startswith(symbols['function_declaration'])


# Removes all whitespace and newline characters from a string
def trim_line(line: str) -> str:
    
    return line.rstrip('\n').replace(' ', '')


# Converts a line string into components, where components are
# strings, separated by the into symbol
def line_to_components(line: str) -> list:

    return line.split(symbols['into'])


# Determine what type a word is from a given word string
def get_word_type(word: str) -> str:

    # If a word is a digit, it is a value
    if word.isdigit():
        return 'value'

    # If the word contains any other digits or special characters, it is invalid
    elif not word.isalpha():
        return 'invalid'

    # If the word is all lowercase, then it is a flag
    elif word.islower():
        return 'flag'

    # If the word is all uppercase, then it is a function
    elif word.isupper():
        return 'function'

    # Uncaught words are invalid
    else:
        return 'invalid'


# Returns False if '0', True if '1', and None if other
def value_to_boolean(word: str):
    if word == '0':
        return False
    elif word == '1':
        return True
    else:
        return None


# Take a list of words and convert them all to values
# Returns a list of values if parsed, and None if something failed
def get_values_from_word_list(word_list: list):

    value_list = []
    for word in word_list:

        # Get the word type for processing
        word_type = get_word_type(word)

        # First check if the word is a raw value
        if word_type == 'value':

            # Get the value of the word as a boolean
            value = value_to_boolean(word)

            if value == None:

                # If the value is None, it is not a valid boolean word
                errors.word_is_not_valid_input(word)
                return None

            else:

                # Add the value to the list
                value_list.append(value)

        # Then check if it is an existing, assigned flag
        elif word_type == 'flag':
            
            # Get the value from the global flag dictionary
            try:

                # Add that flag's value to the list
                value_list.append(data.flags[word])

            except KeyError:

                # The flag has not been iitialised yet
                errors.flag_is_not_initialised(word)
                return None

        # If it is not a value or a flag, it is not a valid input
        else:

            errors.word_is_not_valid_input(word)
            return None

    return value_list


# Take a list of words and convert them to flags
# Returns a list of flags or None if parsing failed
def get_flags_from_word_list(word_list: list):

    # Because a word list is just a list of strings, and a flag
    # is a string, then any word list where all words are valid
    # flags can simply be returned

    for word in word_list:

        if get_word_type(word) != 'flag':

            errors.word_is_not_valid_flag(word)
            return None

    return word_list