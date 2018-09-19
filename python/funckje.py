#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szablon.py
#  


def hello():
    print("Siema jestem Pyton")
    print("Jak masz na imię?")
    imie = input("odpowiedź:")
    print("Witaj" , imie )
    
def suma(l1,l2):
    print("Suma:" , l1 + l2)



def suma2(a,b):
    """
    Funkcja sumuje dwie liczby i zwraca wynik
    """
    return a + b
    
def roznica(l1,l2):
    
    print("roznica:" , l1- l2)
def iloczyn(l1,l2):
    print("iloczyn:" , l1 * l2)
def iloraz(l1,l2):
    print("ioloraz:" , l1 / l2)
    
    

    
def main(args):
    a = int(input("Podaj 1. liczbę: "))
    print(a)
    b = int(input ("Podaj 2. liczbę: "))
    print(b)
    
    print("suma:" , suma2(a,b))
    #suma(a,b)
    # print("Suma:" , a + b)
    roznica(a,b)
    # print("Roznica:" , a - b)
    iloczyn(a,b)
    # print("Iloczyn:" , a * b)
    iloraz(a,b)
    # print("Iloraz:" , a / b)
    hello() 
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))



