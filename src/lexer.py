
import ply.lex as lex
import decimal

#RESERVED WORDS


reserved_words = {

    'start': 'START',

    'makeWindow': 'MAKEWINDOW',

    'switch': 'SWITCH',

    'background':'BACKGROUND',

    'check': 'CHECK',

    'button': 'BUTTON',

    'oval': 'OVAL',

    'square': 'SQUARE',

    'reset': 'RESET',

    'line': 'LINE',

    'update': 'UPDATE',

    'label': 'LABEL'
}

# tokens defined

tokens = ['CURL_L','CURL_R','COMMA', 'PERIOD', 'NUMBER','IDENTIFIER'] \
         + list(reserved_words.values())

# Rules for tokens

t_PERIOD = r'\.'
t_COMMA = r'\,'

reserved_words_map = { }

for r in reserved_words:
    reserved_words_map[r.lower()] = r


# Find the identifiers
def t_IDENTIFIER(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Checking the reserved words
    token.type = reserved_words.get(token.value, 'IDENTIFIER')
    return token



def t_NUMBER(token):
    r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
    token.value = decimal.Decimal(token.value)
    return token

def t_NLINE(token):
    r'\n+'
    token.lexer.lineno += len(token.value)
    return token


def t_WS(token):
    r' [ ]+ '


def t_CURL_L(token):
    r'\{'
    return token


def t_CURL_R(token):
    r'\}'
    return token



# Ignored characters
token_ignore = ' \t'


# Error handling rule
def t_error(token):
    print("Illegal character '%s'" % token.value[0], token.lineno)
    token.lexer.skip(1)


lexer = lex.lex()
