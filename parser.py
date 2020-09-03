
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

def lista():
    print("----LISTA")
    if token == LRP:
        match(LRP)
        lista()
        match(RRP)
    elif token == SIM or token == DIG or token == BOL or token == STR:
        match(token)


def prog():
    print("hola programa")
    print(token)
    if token == LRP:
        # match(token)
        lista()
        match(RRP)
    elif token == SIM or token == DIG or token == BOL or token == STR:
        match(token)
        prog()
    else:
        error("Expresion mal terminada")
    
# Función principal: implementa el análisis sintáctico
def parser():
    global token 
    token = obten_token() # inicializa con el primer token
    print(f"el primer token es {token}")
    print("")
    prog()
    if token == END:
        print("Expresion bien construida!!")
    else:
        error("expresion mal terminada")

parser()