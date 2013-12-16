"""
Given all letters in the english alphabet organized alphabetically
in a 2d array find the shortest path to spell any word by navigating
the 2d array via a combination of up, down, left and right movements.

For example, a 3 x 9 "keyboard" would look like this:

 a b c d e f g h i
 j k l m n o p q r
 s t u v w x y z

In this case, the word 'zebra' would consist of the following indicies:

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
    Print keyboard to the screen.
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
    keyboard = make_keyboard(n_rows, n_columns)
    v = 0
    h = 0
    indicies = []
    for c in commands:
        v += c[0]
        v = v % n_rows
        h += c[1]
        h = h % n_columns
        indicies.append((v, h))
    #print indicies
    word = ""
    for i in indicies:
        word += keyboard[i[0]][i[1]]
    return word


def shortest_path(n_rows, n_columns, string):
    """for each character in the string calculate the shortest x and
    y path for each letter"""
    key_map = make_keymap(n_rows, n_columns)
    commands = []
    print string
    string = 'a' + string #start at the letter 'a' (0, 0)
    for i in range(1, len(string)):
        c1 = string[i - 1]
        c2 = string[i]
        vertical = direction(key_map[c1][0], key_map[c2][0], n_rows)
        horizontal = direction(key_map[c1][1], key_map[c2][1], n_columns)
        commands.append((vertical, horizontal))

    return commands


def direction(pos1, pos2, nPos):
    if pos2 > pos1:
        res1 = pos2 - pos1
        res2 = pos1 + nPos - pos2
        if res2 < res1:
            return -res2
        else:
            return res1
    else:
        res1 = pos1 - pos2
        res2 = pos2 + nPos - pos1
        if res2 < res1:
            return res2
        else:
            return -res1


def direction2(pos1, pos2, nPos):
    """alternate implementation"""
    p1 = pos1
    p2 = pos2
    sign = 1
    if pos2 < pos1:
        sign = -1
    res1 = sign * (p2 - p1)
    res2 = sign * (p1 - p2) + nPos
    if res2 < res1:
        return -sign * res2
    else:
        return sign * res1


if __name__ == "__main__":
    rows = 3
    columns = 9
    word = 'xylophone'
    commands = shortest_path(rows, columns, word)
    keyboard_word = commands_to_word(rows, columns, commands)
    print word
    print commands
    assert(keyboard_word == word)
    print_keyboard(make_keyboard(rows, columns))
