import ply.lex as lex

# List of token names
tokens = (
    'SELECT', 'WHERE', 'LIMIT',  # Keywords
    'VAR', 'IRI', 'STRING',  # Identifiers and literals
    'PREFIXED_NAME',  # Handles dbo:MusicalArtist, foaf:name
    'LBRACE', 'RBRACE', 'DOT',  # Symbols
    'COLON', 'NUMBER'
)


# Token rules
def t_SELECT(t):
    r'SELECT'
    return t

def t_WHERE(t):
    r'WHERE'
    return t

def t_LIMIT(t):
    r'LIMIT'
    return t

def t_VAR(t):
    r'\?[a-zA-Z_]\w*'
    return t

def t_IRI(t):
    r'<[^<>\\s]+>'
    return t

def t_STRING(t):
    r'\"[^\"\n]*\"(@[a-zA-Z]+)?'
    return t

def t_PREFIXED_NAME(t):
    r'[a-zA-Z]+:[a-zA-Z_][\w]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'
t_COLON = r':'

# Ignore comments and spaces
t_ignore_COMMENT = r'\#.*'
t_ignore = ' \t\n'

# Handle errors
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()

# Test input
data = '''
SELECT ?nome ?desc WHERE {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
'''

lexer.input(data)

# Print tokens
for tok in lexer:
    print(tok.type, tok.value)
