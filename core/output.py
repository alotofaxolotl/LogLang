import core.data as data

def print_flags() -> None:

    flag_length = 0

    for flag in data.flags:
        
        if len(flag) > flag_length:
            flag_length = len(flag)

    for flag in data.flags:

        padding = ''
        for i in range(flag_length - len(flag)):
            padding += ' '

        print('{}{} <- {}'.format(flag, padding, int(data.flags[flag])))