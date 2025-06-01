from compra_lex import tokens
import ply.yacc as yacc

import unicodedata

def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')


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

# Regras da gramática
def p_expression_lista(p):
    'lista : catgs'
    p[0] = p[1]
    print(f"Lista Final: {p[1]}")

def p_expression_catgs(p):
    'catgs : catgs catg'
    p[0] = p[1] + [p[2]]

def p_expression_one_catg(p):
    'catgs : catg'
    p[0] = [p[1]]

def p_expression_catgs_empty(p):
    'catgs :'
    p[0] = []

def p_expression_catg(p):
    'catg : CATG POINT products'
    p[0] = {"categoria": p[1], "produtos": p[3]}

def p_expression_products(p):
    'products : products product'
    p[0] = p[1] + [p[2]]

def p_expression_products_one(p):
    'products : product'
    p[0] = [p[1]]

def p_expression_product(p):
    'product : LINE NUM DPOINT PRODUCT DPOINT PRICE DPOINT NUM VIRG'
    p[0] = {"id": p[2], "produto": p[4], "preco": p[6], "quantidade": p[8]}

def p_error(p):
    if p:
        print(f'Erro na expressão: {p.value}')
    else:
        print("Erro de sintaxe inesperado.")

print(tokens)

parser = yacc.yacc()
lista = remover_acentos(lista)
# Testando o parser
parser.parse(lista)
