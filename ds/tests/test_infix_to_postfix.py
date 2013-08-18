import unittest
from strings.infix_to_postfix import infix_to_postfix


class TestInfixPostfix(unittest.TestCase):

    def test_empty_input(self):
        self.assertRaises(ValueError, infix_to_postfix, None)
        self.assertRaises(ValueError, infix_to_postfix, '')

    def test_correct_short_input(self):
        inp = 'A + B'
        self.assertEqual(infix_to_postfix(inp), 'AB+')

    def test_correct_short_input_with_parantheses(self):
        inp = '( A + B )'
        self.assertEqual(infix_to_postfix(inp), 'AB+')


    def test_correct_long_input(self):
        inp = 'A * B + C * D'
        self.assertEqual(infix_to_postfix(inp), 'AB*CD*+')

    def test_correct_long_input_with_parentheses(self):
        inp = '( A * B ) + C * D'
        self.assertEqual(infix_to_postfix(inp), 'AB*CD*+')



if __name__ == '__main__':
    unittest.main()
