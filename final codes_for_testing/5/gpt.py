import unittest
from c import Token, Lexer, Parser, Interpreter
class TestInterpreter(unittest.TestCase):
    def test_evaluate_expression(self):
        self.assertEqual(evaluate_expression("1+2"), 3)
        self.assertEqual(evaluate_expression("3-1"), 2)
        self.assertEqual(evaluate_expression("2*3"), 6)
        self.assertEqual(evaluate_expression("6/2"), 3)
        self.assertEqual(evaluate_expression("1+2*3"), 7)
        self.assertEqual(evaluate_expression("(1+2)*3"), 9)
        self.assertEqual(evaluate_expression("1+(2*3)"), 7)
        self.assertEqual(evaluate_expression("1+(2*3)/3"), 3)
        self.assertEqual(evaluate_expression("1+(2*3)/0"), ZeroDivisionError)
        self.assertEqual(evaluate_expression("-1"), -1)
        self.assertEqual(evaluate_expression("-1+2"), 1)
        self.assertEqual(evaluate_expression("-1+2*3"), 5)

if __name__ == '__main__':
    unittest.main()