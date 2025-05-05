import operator

class Token:
    NUMBER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = (
        'NUMBER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LPAREN', 'RPAREN', 'EOF'
    )

    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}"


class Lexer:
    def __init__(self, text):
        self.text = text.replace(" ", "")
        self.pos = 0
        self.current_char = self.text[0] if self.text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def generate_tokens(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isdigit() or self.current_char == '.':
                tokens.append(self.generate_number())
            elif self.current_char == '+':
                tokens.append(Token(Token.PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(Token.MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(Token.MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(Token.DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(Token.LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(Token.RPAREN))
                self.advance()
            else:
                raise Exception(f"Illegal character: {self.current_char}")
        tokens.append(Token(Token.EOF))
        return tokens

    def generate_number(self):
        num_str = ''
        dot_count = 0
        while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
            num_str += self.current_char
            self.advance()
        return Token(Token.NUMBER, float(num_str))


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = tokens[0]

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.pos += 1
            self.current_token = self.tokens[self.pos]
        else:
            raise Exception(f"Unexpected token: {self.current_token}")

    def parse(self):
        return self.expr()

    def expr(self):
        result = self.term()
        while self.current_token.type in (Token.PLUS, Token.MINUS):
            if self.current_token.type == Token.PLUS:
                self.eat(Token.PLUS)
                result = ('+', result, self.term())
            elif self.current_token.type == Token.MINUS:
                self.eat(Token.MINUS)
                result = ('-', result, self.term())
        return result

    def term(self):
        result = self.factor()
        while self.current_token.type in (Token.MUL, Token.DIV):
            if self.current_token.type == Token.MUL:
                self.eat(Token.MUL)
                result = ('*', result, self.factor())
            elif self.current_token.type == Token.DIV:
                self.eat(Token.DIV)
                result = ('/', result, self.factor())
        return result

    def factor(self):
        token = self.current_token
        if token.type == Token.NUMBER:
            self.eat(Token.NUMBER)
            return token.value
        elif token.type == Token.LPAREN:
            self.eat(Token.LPAREN)
            result = self.expr()
            self.eat(Token.RPAREN)
            return result
        elif token.type == Token.MINUS:
            self.eat(Token.MINUS)
            return ('neg', self.factor())
        raise Exception(f"Unexpected token in factor: {token}")


class Interpreter:
    def evaluate(self, node):
        if isinstance(node, float):
            return node
        elif isinstance(node, tuple):
            if node[0] == '+':
                return self.evaluate(node[1]) + self.evaluate(node[2])
            elif node[0] == '-':
                return self.evaluate(node[1]) - self.evaluate(node[2])
            elif node[0] == '*':
                return self.evaluate(node[1]) * self.evaluate(node[2])
            elif node[0] == '/':
                divisor = self.evaluate(node[2])
                if divisor == 0:
                    raise ZeroDivisionError("Division by zero")
                return self.evaluate(node[1]) / divisor
            elif node[0] == 'neg':
                return -self.evaluate(node[1])
        raise Exception("Invalid node")


def evaluate_expression(expr):
    lexer = Lexer(expr)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    return interpreter.evaluate(ast)
