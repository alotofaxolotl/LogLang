import sys

import core.errors as errors
import core.logic as logic
import core.parser as parser
import core.runner as runner
import core.output as output

from core.compound_function import compound_function as cf

import core.data as data

# Ensures that the command entered by the user contains
# the right amount of arguments
def validate_command() -> bool:
    
    # If there were less than 2 arguments, return False
    return len(sys.argv) >= 2

# Tells the parser whether to parse a line or add the line to a compound function
defining_function = False

# Properties for a compound function
c_name = ''
c_in_size = ''
c_out_size = ''
c_lines = []

def parse_line(line: str) -> None:

    global defining_function, c_name, c_in_size, c_out_size, c_lines

    # Remove unecessary characters from the line
    trimmed_line = parser.trim_line(line)

    # If the line is a comment or blank, skip it
    if parser.is_line_comment(trimmed_line) or trimmed_line == '':

        return

    # If the line is a function declaration, we need to get funky!
    if parser.is_line_function_declaration(trimmed_line):

        defining_function = not defining_function
        if defining_function:

            try:

                # This line is the declarative line for the new function
                trimmed_line = trimmed_line.replace('$', '')

                c_name = trimmed_line.split('(')[0]
                raw_size = trimmed_line.split('(')[1].replace(')', '')

                c_in_size = int(raw_size.split(',')[0])
                c_out_size = int(raw_size.split(',')[1])

            except Exception:

                errors.function_failed_define()

        else:

            # We are finished defining the function so add it to the dict
            data.compound_functions[c_name] = cf(c_name, c_in_size, c_out_size, c_lines)
            c_name = ''
            c_in_size = ''
            c_out_size = ''
            c_lines = []

        return


    if defining_function:
        # Just add the line to the list and return
        c_lines.append(line)
        return

    # Get the components from a line
    components = parser.line_to_components(trimmed_line)

    # If the line has one component, it must be an empty assignment line
    # eg. 'a, b, c'
    if len(components) == 1:
        
        # Tell the interpreter to stop if the line failed
        if not runner.empty_assignment(components):
            data.exit_flag = True

        return

    # If the line has two components, it must be a value assignment line
    # eg. '0 -> a' or '0, 1 -> a, b, c, d'
    elif len(components) == 2:

        # Tell the interpreter to stop if the line failed
        if not runner.value_assignment(components):
            data.exit_flag = True

        return

    # If the line has three components, it must be a function call
    # eg. '0, 1 -> AND -> a'
    elif len(components) == 3:

        # Tell the interpreter to stop if the line failed
        if not runner.function_call(components):
            data.exit_flag = True

        return

    # No line can have more than 3 components, so it must not be valid
    else:

        errors.line_is_not_valid(line)
        data.exit_flag = True
        return


def main():
    
    # Check if the command inputed by the user is valid
    if not validate_command():
        
        # Break if it isn't
        errors.insufficient_arguments()
        return

    # The filename is the second argument, loglang.py is the first
    file_name = sys.argv[1]

    # Open the file specified by the user
    try:

        with open(file_name, 'r') as file:
            
            line_counter = 0

            for line in file:

                line_counter += 1
                parse_line(line)

                # Break if needed
                if data.exit_flag:
                    print('{}: {}'.format(line_counter, line))
                    return

    except FileNotFoundError:

        # The file does not exist
        errors.file_not_found(file_name)
        return

    # After execution, print the flags
    output.print_flags()


if __name__ == '__main__':
    main()