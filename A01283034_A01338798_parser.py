
# INTEGRANTES
# Edgar Rubén Salazar Lugo A01338798
# Jorge Alexander Giovannetti Pulido A01283034


# Gramática del parser
# <prog> ::= <exp> <prog> | $
# <exp> ::= <átomo>| <lista>
# <átomo> ::=símbolo | <constante>
# <constante> ::= número| booleano| string
# <lista> ::= ( <elementos>)
# <elementos> ::= <exp> <elemento> | 

import sys
from A01283034_A01338798_scanner import (
    obten_token,
    BOL,
    SIM,
    STR,
    DIG,
    LRP,
    RRP,
    END,
    ERR
)

def error():
    print(">>ERROR SINTACTICO<<")
    sys.exit(1)

def match(tokenEsperado):
    global token
    if token == tokenEsperado:
        token = obten_token()
    else:
        error()

def prog():
    if(token == END):
        return
    else:
        exp()
        prog()

def exp():
    if token == LRP:
        lista()
    else:
        atomo()

def atomo():
    if token == SIM:
        match(token)
    else:
        constante()

def constante():
    if token == DIG or token == BOL or token == STR:
        match(token)
    else:
        error()

def lista():
    match(LRP)
    elementos()
    match(RRP)

def elementos():
    if(token != RRP):
        exp()
        elementos()
        
# Función principal: implementa el análisis sintáctico
def parser():
    global token 
    token = obten_token() # inicializa con el primer token
    prog()
    if token == END:
        print(">>ENTRADA CORRECTA<<")
    else:
        error()

parser()