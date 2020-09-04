  
# INTEGRANTES
# Edgar Rubén Salazar Lugo A01338798
# Jorge Alexander Giovannetti Pulido A01283034

import sys

# tokens
BOL = 100  # Booleano
SIM = 101  # Símbolo
STR = 102  # String
DIG = 103  # Digito

LRP = 104  # Delimitador: paréntesis izquierdo
RRP = 105  # Delimitador: paréntesis derecho

END = 300
ERR = 200

#        #   t/f  letra  "   dig  esp   (    )  raro   \n   $  
MT = [[   1,   2,   2,   3,   4,   0, LRP, RRP,   5,   0, END], # edo 0 - estado inicial
      [ ERR, BOL, ERR, ERR, ERR, ERR, ERR, ERR,   5, ERR, ERR], # edo 1 - booleanos
      [ ERR,   2,   2, ERR, ERR, SIM, SIM, SIM,   5, SIM, SIM], # edo 2 - símbolos
      [ ERR,   3,   3, STR,   3,   3, ERR, ERR, ERR,   3, ERR], # edo 3 - strings
      [ ERR, ERR, ERR, ERR,   4, DIG, DIG, DIG, ERR, DIG, DIG], # edo 4 - digitos
      [ ERR, ERR, ERR, ERR, ERR, ERR, ERR, ERR,   5, ERR, ERR]  # edo 5 - ERROR
    ]


def filtro(c):
    if c == '#':
        return 0
    elif c == 't' or c == 'f':
        return 1
    elif (c >= 'a' and c <= 'z'):
        return 2
    elif c == '"':
        return 3
    elif c == '0' or c == '1' or c == '2' or \
       c == '3' or c == '4' or c == '5' or \
       c == '6' or c == '7' or c == '8' or c == '9':
        return 4
    elif c == ' ' or ord(c) == 9 or ord(c) == 10 or ord(c) == 13: # blancos
        return 5
    elif c == '(':
        return 6
    elif c == ')':
        return 7
    elif c == '\n':
        return 9
    elif c == '$':
        return 10    
    else: 
        return 8

_c = None    # siguiente caracter
_leer = True # indica si se requiere leer un caracter de la entrada estándar

def obten_token():
    global _c, _leer
    edo = 0 # número de estado en el autómata
    lexema = "" # palabra que genera el token
    while (True):
        while edo < 100:    # mientras el estado no sea ACEPTOR ni ERROR
            if _leer: _c = sys.stdin.read(1)
            else: _leer = True
            edo = MT[edo][filtro(_c)]
            if edo < 100 and edo != 0: lexema += _c
        if edo == DIG:    
            _leer = False # ya se leyó el siguiente caracter
            print("Digito", lexema)
            return DIG
        elif edo == BOL:   
            lexema += _c # el último caracter forma el lexema
            print("Booleano", lexema)
            return BOL
        elif edo == SIM:   
            _leer = False # ya se leyó el siguiente caracter
            print("Simbolo", lexema)
            return SIM
        elif edo == STR:   
            lexema += _c    
            print("String", lexema)
            return STR
        elif edo == LRP:   
            lexema += _c  # el último caracter forma el lexema
            print("Delimitador", lexema)
            return LRP
        elif edo == RRP:  
            lexema += _c  # el último caracter forma el lexema
            print("Delimitador", lexema)
            return RRP
        elif edo == END:
            print("Fin de expresion")
            return END
        else:   
            _leer = False # el último caracter no es raro
            print(">>ERROR LEXICO<<")
            return ERR
            