import re

# replace all the dots with new line "\n", if the dots are not within double quotation marks
def replace_dots(string): 
    '''
    compile a regular expression pattern into a regular expression obejct.
    In the re.compile function, the "r" indicates that the string should be treated as raw string, so backslash is used literally.
    The backslash is used for dot to be treated as literal dot, and not as metacharacter in regular expression
    '(?=(?:[^"]*"[^"]*")*[^"]*$)': a positive lookahead assertion, which checks that the dot is outside a pair of double quotation marks
    '''
    pattern = re.compile(r'\.(?=(?:[^"]*"[^"]*")*[^"]*$)')

    # use the compiled pattern to replace all the dots with new line, if the dots are not within double quotation marsk
    replaced = pattern.sub('.\n', string)
    return replaced


# adding new line after n chars. After n chars, if it is not white-space, put new line when seeing the next white-space
def add_newline_after_n_chars(string, n):
    lines = string.split('\n') # split string into list of lines whenever encountering new line
    updated_lines = []

    for line in lines:
        words = line.split() # split current line into list of words
        current_line = ''

        for word in words:
            if len(current_line) + len(word) <= n: # checking if adding the current word would exceed n
                current_line += word + ' ' # adding current word to current line
            else:
                updated_lines.append(current_line.strip()) # append the current line to the list
                current_line = word + ' ' # making a new current line

        updated_lines.append(current_line.strip()) # appending the last line

    return '\n'.join(updated_lines) # join all the modified lines into a string with new line between the lines

