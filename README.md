Keyboard Shortest Path Code
======================

Given all letters in the english alphabet organized alphabetically
in a 2d array find the shortest path to spell any word by navigating
the 2d array with a combination of up, down, left and right movements.

For example, a 3 x 9 "keyboard" would look like this:
~~~
 a b c d e f g h i
 j k l m n o p q r
 s t u v w x y z
~~~
In this case, the word `zebra` is comprised of the following indicies:
~~~
[(2, 7), (0, 4), (0, 1), (1, 8), (0, 0)]
~~~
The shortest path for this word, starting at the letter `a` is:
~~~
[(-1, -2), (1, -3), (0, -3), (1, -2), (-1, 1)]
~~~
where negative represents up or left and positive represents down or right.

So, `(-1, -2)` means move 1 row up and 2 columns to the left or:
~~~
up, left, left
~~~ 
which moves the cursor from the letter `a` at `(0, 0)` to the letter `z` at `(2, 7)`.

