"""
Given all letters in the english alphabet organized alphabetically
in a 2d array find the shortest path to spell any word by navigating
the 2d array via a combination of up, down, left and right movements.

For example, a 3 x 9 "keyboard" would look like this:

 a b c d e f g h i
 j k l m n o p q r
 s t u v w x y z

In this case, the word 'zebra' would consist of the following indices:

 [(2, 7), (0, 4), (0, 1), (1, 8), (0, 0)]

The shortest path for this word, starting a the letter 'a' is:

 [(-1, -2), (1, -3), (0, -3), (1, -2), (-1, 1)]

Where negative represents up or left.

So, (-1, -2) means move 1 row up and 2 columns to the left
or "up, left, left" which puts the cursor on the letter 'z' at (2, 7).
"""


def make_keyboard(n_rows, n_columns):
    """
    Make an alphabetical keyboard.
    """
    start = 97
    assert(n_columns * n_rows >= 26)
    a = [['' for j in range(n_columns)] for i in range(n_rows)]
    for i in range(n_rows):
        for j in range(n_columns):
            if start < 97 + 26:
                a[i][j] = unichr(start)
                start += 1
    return a


def print_keyboard(keyboard):
    """
    Print keyboard nicely to the screen.
    """
    for i in range(len(keyboard)):
        row = ""
        for j in range(len(keyboard[i])):
            row += " " + keyboard[i][j]
        print row


def make_keymap(n_rows, n_columns):
    """
    Map characters to a tuple of x,y cooridnates in a keyboard array.
    """
    start = 97
    assert(n_columns * n_rows >= 26)
    a = {}
    for i in range(n_rows):
        for j in range(n_columns):
            if start < 97 + 26:
                a[unichr(start)] = i, j
                start += 1
    return a


def commands_to_word(n_rows, n_columns, commands):
    """
    given a list of commands and the dimensions of a keyboard convert the
    commands to letters. assumes we start at the letter 'a' (0, 0)
    """
    keyboard = make_keyboard(n_rows, n_columns)
    v = 0
    h = 0
    indices = []
    for c in commands:
        v += c[0]
        v = v % n_rows
        h += c[1]
        h = h % n_columns
        indices.append((v, h))
    word = ""
    for i in indices:
        word += keyboard[i[0]][i[1]]
    return word


def shortest_path(n_rows, n_columns, string):
    """
    for each character in the string calculate the shortest x and
    y path for each letter
    """
    key_map = make_keymap(n_rows, n_columns)
    commands = []
    #start at the letter 'a' (0, 0)
    string = 'a' + string
    for i in range(1, len(string)):
        c1 = string[i - 1]
        c2 = string[i]
        vertical = distance(key_map[c1][0], key_map[c2][0], n_rows)
        horizontal = distance(key_map[c1][1], key_map[c2][1], n_columns)
        commands.append((vertical, horizontal))

    return commands


def distance(pos1, pos2, nPos):
    """
    gets the shortest distance between 2 indices in an array accounting
    for wrapping
    """
    res1 = (pos2 - pos1) % nPos
    res2 = (pos1 - pos2) % nPos
    if res1 < res2:
        return res1
    else:
        return -res2


if __name__ == "__main__":
    rows = 3
    columns = 9
    word = 'python'
    commands = shortest_path(rows, columns, word)
    keyboard_word = commands_to_word(rows, columns, commands)
    print word
    print commands
    assert(keyboard_word == word)
    print_keyboard(make_keyboard(rows, columns))
