import keyboard_shortest_path as kps
import unittest


class test_shortest_path(unittest.TestCase):

    def setUp(self):
        pass

    def test_zebra_3x9(self):
        rows = 3
        columns = 9

        commands = kps.shortest_path(rows, columns, 'jeff')
        self.assertEqual(commands, [(1, 0), (-1, 4), (0, 1), (0, 0)])
        word = kps.commands_to_word(rows, columns, commands)
        self.assertEqual(word, 'jeff')

        commands = kps.shortest_path(rows, columns, 'zebra')
        self.assertEqual(commands,
                         [(-1, -2), (1, -3), (0, -3), (1, -2), (-1, 1)])
        word = kps.commands_to_word(rows, columns, commands)
        self.assertEqual(word, 'zebra')
        #kps.print_keyboard(kps.make_keyboard(rows, columns))


if __name__ == '__main__':
        unittest.main()
