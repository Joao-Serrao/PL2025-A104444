# listas_lex.py
# -*- coding: utf-8 -*-
import ply.lex as lex

lista = """CARNE :
  - 1 :: Bife :: 10.00 :: 1;
  - 2 :: Panado :: 5.00 :: 4;
  - 3 :: Hambúrguer :: 8.00 :: 3;
  - 4 :: Almôndegas :: 7.00 :: 5;

BEBIDA :
  - 5 :: Água :: 0.40 :: 16;
  - 6 :: Sumo :: 1.50 :: 9;
  - 7 :: Refrigerante :: 1.80 :: 10;

FRUTA :
  - 8 :: Maçã :: 0.60 :: 20;
  - 9 :: Banana :: 0.50 :: 15;
  - 10 :: Laranja :: 0.80 :: 18;
  - 11 :: Pêssego :: 0.70 :: 22;
  - 12 :: Uva :: 0.90 :: 17;

LEGUMES :
  - 13 :: Alface :: 1.00 :: 25;
  - 14 :: Tomate :: 0.75 :: 23;
  - 15 :: Cebola :: 0.50 :: 28;
  - 16 :: Batata :: 0.30 :: 30;
  - 17 :: Cenoura :: 0.40 :: 26;

PASTELARIA :
  - 18 :: BolodeChocolate :: 3.50 :: 1;
  - 19 :: Croissant :: 1.20 :: 14;
  - 20 :: PasteldeNata :: 1.00 :: 5;
  - 21 :: Donut :: 0.80 :: 13;"""

tokens = ['CATG', 'POINT', 'LINE', 'NUM', 'DPOINT', 'PRODUCT', 'PRICE', 'VIRG']

# Define tokens as functions for better processing

def t_CATG(t):
    r'[A-Z][A-Z]+'
    t.value = t.value.strip(' :')  # Remove spaces and colon
    return t

def t_PRODUCT(t):
    r'[A-Za-zÀ-ÿ]+'
    t.value = t.value.strip(': ').strip()
    return t

def t_PRICE(t):
    r'(\d+\.\d{2})'
    t.value = float(t.value)
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value.replace("-", "").replace("::", "").strip())
    return t


def t_DPOINT(t):
    r'::'
    return t

def t_POINT(t):
    r':'
    return t


def t_LINE(t):
    r'-'
    return t

def t_VIRG(t):
    r';'
    return t

# Ignore spaces, tabs, and newlines
t_ignore = " \t\n"

# Error handling
def t_error(t):
    print('Caráter ilegal:', t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

lexer.input(lista)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)