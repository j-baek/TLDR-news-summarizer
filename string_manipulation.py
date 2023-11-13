import re

# replace all the dots with new line "\n", if the dots are not within double quotation marks
def replace_dots(string): 
    '''
    compile a regular expression pattern into a regular expression obejct.
    In the re.compile function, the "r" prefix indicates that the backslash should be treated as a literal backslash,
    and backslash itself indicates that the dot should be used as a literal dot, and not a metacharacter
    Metacharacter is a character that has a special meaning and is not treated as a literal character
    '(?=(?:[^"]*"[^"]*")*[^"]*$)': a positive lookahead assertion, which checks if the dot is outside a pair of double quotation marks
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

# combine news and url together, with url having a hyperlink
def news_info_and_url(news, url):
    combined = ''
    
    # iterate both news and url at the same time using zip function,
    # and put news element and url element together with url having a hyperlink
    for news_e, url_e in zip(news,url):
        combined += f'{news_e} <a href="{url_e}">{url_e}</a>' #f is for formatted string
    return combined