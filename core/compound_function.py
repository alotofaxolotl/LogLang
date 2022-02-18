# A compund function is a user defined function that consists of multiple
# function call lines.

import core.parser as parser
import core.logic as logic

class compound_function:

    def __init__(self, name: str, in_size: int, out_size: int, lines: list) -> None:

        self.name = name
        self.in_size = in_size
        self.out_size = out_size
        self.lines = lines
        self.flags = {}


    def error(self):
        print('{} failed!'.format(self.name))


    def compute(self, values: list):

        # Create a new list of values for the output
        result = []
        for i in range(self.out_size):
            result.append(False)

        for line in self.lines:

            # Remove unecessary characters from the line
            trimmed_line = parser.trim_line(line)

            # If the line is a comment or blank, skip it
            if parser.is_line_comment(trimmed_line) or trimmed_line == '':

                return

            # Get the components from a line
            components = parser.line_to_components(trimmed_line)

            # Internal assignment cannot use external flags
            # only lines such as '0 -> a' are valid
            if len(components) == 2:

                # Parse the value words
                value_words = components[0].split(',')
                valid_values = []
                for word in value_words:

                    value = parser.value_to_boolean(word)
                    if value == None:
                        return None

                    valid_values.append(value)

                # Parse the flag words
                flag_words = components[1].split(',')
                valid_flags = []
                for word in flag_words:

                    if parser.get_word_type(word) != 'flag':
                        return None

                    valid_flags.append(word)

                # Store the values internally
                valid_values = logic.trim_values(valid_values, len(valid_flags))
                for i in range(len(valid_flags)):
                    self.flags[valid_flags[i]] = valid_values[i]

            # The only other available line is a function call
            if len(components) == 3:
            
                # Construct a list of input values
                value_words = components[0].split(',')
                valid_values = []

                for value in value_words:
                    if value.isdigit():
                        try:
                            valid_values.append(values[int(value)])
                        except IndexError:
                            self.error
                            return None
                    else:
                        try:
                            valid_values.append(self.flags[value])
                        except KeyError:
                            self.error
                            return None

                # Call the logical function specified and store its output
                # determine the function to be called and call it
                logic_function = logic.get_function_from_word(components[1])
                if logic_function == None:
                    self.error
                    return None

                output = logic_function(valid_values)
                if output == None:
                    self.error
                    return None

                targets = components[2].split(',')

                output = logic.trim_values(output, len(targets))

                # Assign outputs accordingly
                for i in range(len(targets)):
                    target = targets[i]
                    if target.isdigit():
                        try:
                            result[int(target)] = output[i]
                        except IndexError:
                            self.error
                            return None
                    elif parser.get_word_type(target) == 'flag':
                        self.flags[target] = output[i]
                    else:
                        self.error
                        return None

        return result
