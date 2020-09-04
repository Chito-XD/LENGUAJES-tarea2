import sys
from scanner import (
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

# Gramática del parser
# <prog> ::= <exp> <prog> | $
# <exp> ::= <átomo>| <lista>
# <átomo> ::=símbolo | <constante>
# <constante> ::= número| booleano| string
# <lista> ::= ( <elementos>)
# <elementos> ::= <exp> <elemento> | 

# Termina con un mensaje de error
def error(mensaje):
    print("ERROR:", mensaje)
    sys.exit(1)

def match(tokenEsperado):
    global token
    if token == tokenEsperado:
        token = obten_token()
    else:
        error("token equivocado")


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
        error("Expresion mal construida: constante no encontrada")

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
        print("Expresion bien construida!!")
    else:
        error("expresion mal terminada 1")

parser()