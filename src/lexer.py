import decimal
import ply.lex as lex




#Reserved words stated
reserved_words = {

    'start': 'START',

    'makeWindow': 'MAKEWINDOW',

    'check': 'CHECK',

    'button': 'BUTTON',

    'oval': 'OVAL',

    'square': 'SQUARE',

    'reset' : 'RESET',

    'label': 'LABEL',

    'end' : 'END'

}


tokens = ['CURL_L','CURL_R','COMMA', 'NUMBER'] \
         + list(reserved_words.values())


t_COMMA = r'\,'

reserved_words_map = { }

for r in reserved_words:
    reserved_words_map[r.lower()] = r


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
