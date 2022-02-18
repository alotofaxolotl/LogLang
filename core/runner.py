import core.parser as parser
import core.logic as logic
import core.data as data

# The runner is the interprative part of the program
# It takes components, parses them, and then does something with them

# empty assignment, requires a single component
# returns true on success, false on failure
def empty_assignment(components: list) -> bool:

    # get the raw flags from components and validate them
    word_list = components[0].split(',')
    valid_flags = parser.get_flags_from_word_list(word_list)

    if valid_flags == None:
        return False

    # assign false to each flag and add it to the flag dictionary
    for flag in valid_flags:

        data.flags[flag] = False

    return True


# value assignment, requires 2 components
# returns true on success, false on failure
def value_assignment(components: list) -> bool:

    # get the raw input values and validate them
    value_word_list = components[0].split(',')
    valid_values = parser.get_values_from_word_list(value_word_list)

    if valid_values == None:
        return False

    # get the raw flags and validate them
    flag_word_list = components[1].split(',')
    valid_flags = parser.get_flags_from_word_list(flag_word_list)

    if valid_flags == None:
        return False

    # store each value into each flag
    # start by ensuring there are an equal number of values and flags
    valid_values = logic.trim_values(valid_values, len(valid_flags))
    for i in range(len(valid_flags)):

        data.flags[valid_flags[i]] = valid_values[i]

    return True


# function call, requires 3 components
# returns true on success, false on failure
def function_call(components: list) -> bool:

    # get the raw input values and validate them
    value_word_list = components[0].split(',')
    valid_values = parser.get_values_from_word_list(value_word_list)

    if valid_values == None:
        return False

    # get the raw flags and validate them
    flag_word_list = components[2].split(',')
    valid_flags = parser.get_flags_from_word_list(flag_word_list)

    if valid_flags == None:
        return False

    # determine the function to be called and call it
    logic_function = logic.get_function_from_word(components[1])
    if logic_function == None:
        return False

    result = logic_function(valid_values)
    if result == None:
        return False

    result = logic.trim_values(result, len(valid_flags))

    # store the function result in the valid flags
    for i in range(len(valid_flags)):

        data.flags[valid_flags[i]] = result[i]

    return True