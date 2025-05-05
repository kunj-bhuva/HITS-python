import unittest
from c import Token, Lexer, Parser, Interpreter

class TestToken(unittest.TestCase):
    def test_integer_token(self):
        token = Token(Token.NUMBER, 5)
        self.assertEqual(token.type, Token.NUMBER)
        self.assertEqual(token.value, 5)

    def test_string_token(self):
        token = Token("string", "hello")
        self.assertEqual(token.type, "string")
        self.assertEqual(token.value, "hello")

    def test_boolean_token(self):
        token = Token("boolean")
        self.assertEqual(token.type, "boolean")
        self.assertIsNone(token.value)

    def test_float_token(self):
        token = Token(Token.NUMBER, 3.14)
        self.assertEqual(token.type, Token.NUMBER)
        self.assertEqual(token.value, 3.14)

    def test_identifier_token(self):
        token = Token("identifier")
        self.assertEqual(token.type, "identifier")
        self.assertIsNone(token.value)

class TestLexer(unittest.TestCase):
    def test_numbers_only_input(self):
        lexer = Lexer("12345")
        tokens = lexer.generate_tokens()
        self.assertEqual(tokens, [Token(Token.NUMBER, 12345)])

    def test_numbers_and_operators_input(self):
        lexer = Lexer("1+2+3")
        tokens = lexer.generate_tokens()
        self.assertEqual(tokens, [Token(Token.NUMBER, 1), Token(Token.PLUS), Token(Token.NUMBER, 2), Token(Token.PLUS), Token(Token.NUMBER, 3)])

    # Add more test cases for Lexer to cover edge cases and scenarios

class TestParser(unittest.TestCase):
    def test_simple_arithmetic_expression(self):
        parser = Parser([Token(Token.NUMBER, 1), Token(Token.PLUS), Token(Token.NUMBER, 2)])
        ast = parser.parse()
        self.assertEqual(ast, ('+', 1, 2))

    # Add more test cases for Parser to cover edge cases and scenarios

class TestInterpreter(unittest.TestCase):
    def test_float_node(self):
        interpreter = Interpreter()
        result = interpreter.evaluate(5.0)
        self.assertEqual(result, 5.0)

    def test_addition_node(self):
        interpreter = Interpreter()
        result = interpreter.evaluate(('+', 3.0, 2.0))
        self.assertEqual(result, 5.0)

    # Add more test cases for Interpreter to cover edge cases and scenarios

if __name__ == '__main__':
    unittest.main()
