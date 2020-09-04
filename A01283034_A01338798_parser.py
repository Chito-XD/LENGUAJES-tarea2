
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

# Imports necesarios del otro archivo
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

# Método que genera el error sintáctico
def error():
    print(">>ERROR SINTACTICO<<")
    sys.exit(1)

# Metodo que revisa si el token es el esperado
def match(tokenEsperado):
    global token
    if token == tokenEsperado:
        token = obten_token()
    else:
        error()

# Metodo que evalua la semantica de un programa
def prog():
    if(token == END):
        return
    else:
        exp()
        print("<prog>")
        prog()

# Metodo que evalua la semantica de una expresion
def exp():
    print("<exp>")
    if token == LRP:
        lista()
    else:
        atomo()

# Metodo que evalua la semantica de un atomo
def atomo():
    print("<atomo>")
    if token == SIM:
        match(token)
    else:
        constante()

# Metodo que evalua la semantica de una constante
def constante():
    print("<constante>")
    if token == DIG or token == BOL or token == STR:
        match(token)
    else:
        error()

# Metodo que evalua la semantica de una lista
def lista():
    print("<lista>")
    match(LRP)
    elementos()
    match(RRP)

# Metodo que evalua la semantica de un elemento
def elementos():
    print("<elemento>")
    if(token != RRP):
        exp()
        elementos()
        
# Función principal: implementa el análisis sintáctico
def parser():
    global token 
   
    token = obten_token() # inicializa con el primer token
    print("<prog>")
    prog()
    if token == END:
        # Impresion de una entrada correcta
        print(">>ENTRADA CORRECTA<<")
    else:
        error()

parser()