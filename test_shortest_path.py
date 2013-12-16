import keyboard_shortest_path as ksp
import unittest


class test_shortest_path(unittest.TestCase):

    def setUp(self):
        pass

    def test_zebra_3x9(self):
        rows = 3
        columns = 9

        commands = ksp.shortest_path(rows, columns, 'jeff')
        self.assertEqual(commands, [(1, 0), (-1, 4), (0, 1), (0, 0)])
        word = ksp.commands_to_word(rows, columns, commands)
        self.assertEqual(word, 'jeff')

        commands = ksp.shortest_path(rows, columns, 'zebra')
        self.assertEqual(commands,
                         [(-1, -2), (1, -3), (0, -3), (1, -2), (-1, 1)])
        word = ksp.commands_to_word(rows, columns, commands)
        self.assertEqual(word, 'zebra')
        ksp.print_keyboard(ksp.make_keyboard(rows, columns))


if __name__ == '__main__':
        unittest.main()
