# All logic functions return a list, even if that function only returns a single value
# These functions also assume that the incoming value list is valid and only has booleans

import core.errors as errors
import core.data as data

# Generates a new list of values of a fixed size
# The input ([1, 2, 3, 4, 5], 2) gives [1, 2]
# The input ([1, 2], 3) gives [1, 2, 1]
def trim_values(values: list, size: int) -> list:

    # If there are enough values, return the first 2
    if len(values) > size:
        return values[:size]

    # If there aren't enough values, create a new list and pad it
    # by iterating over the supplied values
    else:

        new_values = []
        for i in range(size):

            # Use modulus to repeat iteration
            new_values.append(values[i%len(values)])

        return new_values


# Returns [True] only if all values are True
def l_and(values: list) -> list:

    for value in values:

        # At least one value is false
        if value == False:

            return [False]

    # None of the values were false
    return [True]


# Returns [True] if at least one value is True
def l_or(values: list) -> list:

    for value in values:

        # At least one value is true
        if value == True:
            
            return [True]

    # None of the values were true
    return [False]


# Returns [True] if none of the inputs are equal
# This is a strict function with 2 inputs
def l_xor(values: list) -> list:

    # Take the input and create an array of length 2
    # This ensures index [1] always exists
    trimmed_values = trim_values(values, 2)

    # If the first and second input are not equal, return [True]
    return [trimmed_values[0] != trimmed_values[1]]


# Returns a list containing the inverse of the supplied values
# [True, False, False, True] becomes [False, True, True, False]
def l_not(values: list) -> list:

    result = []
    for value in values:

        # Flip each value
        result.append(not value)

    return result


# NAND is the same as NOT AND
def l_nand(values: list) -> list:

    # l_not(l_and) will give NAND
    return l_not(l_and(values))


# NOR is the same as NOT OR
def l_nor(values: list) -> list:

    # l_not(l_or) will give NOR
    return l_not(l_or(values))


# XNOR is the same as NOT XOR
def l_xnor(values: list) -> list:

    # l_not(l_or) will give NOT XOR
    return l_not(l_xor(values))


function_words = {
    'AND': l_and,
    'OR': l_or,
    'XOR': l_xor,
    'NOT': l_not,
    'NAND': l_nand,
    'NOR': l_nor,
    'XNOR': l_xnor
}

# Takes a word and returns the associated function
def get_function_from_word(word: str):

    # Check the builtin functions
    try:

        return function_words[word]

    except KeyError:

        # Check compound functions
        try:

            return data.compound_functions[word].compute

        except KeyError:

            # That function doesn't exist
            errors.function_does_not_exist(word)
            return None
