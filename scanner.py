  
# INTEGRANTES
# Edgar Rubén Salazar Lugo A01338798

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

#      bool  letra  "   dig  esp   (    )  raro   \n   $  
MT = [[ BOL,   1,   2,   3,   0, LRP, RRP,   4,   0, END], # edo 0 - estado inicial
      [ ERR,   1, ERR, ERR, SIM, SIM, SIM,   4, SIM, SIM], # edo 1 - símbolos
      [ ERR,   2, STR,   2,   2, ERR, ERR, ERR,   2, ERR], # edo 2 - strings
      [ ERR, ERR, ERR,   3, DIG, DIG, DIG, ERR, DIG, DIG], # edo 3 - digitos
      [ ERR, ERR, ERR, ERR, ERR, ERR, ERR,   4, ERR, ERR]  # edo 4 - ERROR
    ] 


def filtro(c):
    # print(f"ENTRO FILTRO: {c}")
    # print(f"leng: {len(c)}")
    if c == "#t" or c == "#f":
        return 0
    elif len(c) == 2:
        return 7
    elif c == '"':
        return 2
    elif c == '0' or c == '1' or c == '2' or \
       c == '3' or c == '4' or c == '5' or \
       c == '6' or c == '7' or c == '8' or c == '9':
        return 3
    elif c == ' ' or ord(c) == 9 or ord(c) == 10 or ord(c) == 13: # blancos
        return 4
    elif c == '(':
        return 5
    elif c == ')':
        return 6
    elif c == '\n':
        return 8
    elif c == '$':
        return 9
    elif (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
        return 1   
    else: 
        return 7

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
            if _c == "#":
                _c += sys.stdin.read(1)
            edo = MT[edo][filtro(_c)]
            if edo < 100 and edo != 0: lexema += _c
        if edo == DIG:    
            _leer = False # ya se leyó el siguiente caracter
            print("Digito ", lexema)
            return DIG
        elif edo == BOL:   
            # _leer = False # ya se leyó el siguiente caracter
            lexema += _c
            print("Boooleano ", lexema)
            return BOL
        elif edo == SIM:   
            _leer = False # ya se leyó el siguiente caracter
            print("Simbolo ", lexema)
            return SIM
        elif edo == STR:   
            # _leer = False # ya se leyó el siguiente caracter
            lexema += _c
            print("String ", lexema)
            return STR
        elif edo == LRP:   
            lexema += _c  # el último caracter forma el lexema
            print("Delimitador ", lexema)
            return LRP
        elif edo == RRP:  
            lexema += _c  # el último caracter forma el lexema
            print("Delimitador ", lexema)
            return RRP
        elif edo == END:
            print("Fin de expresion")
            return END
        else:   
            _leer = False # el último caracter no es raro
            print("ERROR! palabra ilegal", lexema)
            return ERR
            
obten_token()