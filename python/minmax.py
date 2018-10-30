#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minmax.py

import random 




def losuj(ile, lmin, lmax):
    lista = []
    for i in range(ile):
        lista.append(random.randint(lmin, lmax))
    print(lista)
    return lista




def minmax():
    ile = int(input('Ile podasz liczb?:'))
    min = max = int(input('Podaj liczbe: '))
    for i in range(ile - 1):
        liczba = int(input('Podaj liczbe: ')) 
        
        if min > liczba:
            min = liczba
        if max < liczba:
            max = liczba
    return min , max
    
def minimum(liczby):
    najm = lista[0]
    for i in liczby:
        if najm > i:
            njam = i
    return najm 
    
def main(args):
    # ~najm , najw = minmax()
    # ~print('Najmnijesza: ' , najm)
    # ~print('Najwieksza: ' , najw)
    liczby = losuj(20, 0 , 50)
    print('Najmnijesza: ' , minimum(liczby))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
