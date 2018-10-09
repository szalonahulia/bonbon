#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py

def prostokat1 (a, b, znak):
    for i in range(a):
        for j in range(b):
            print(znak, end='')
        print()
def prostokat2 (a, b, znak):
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b-1 or i ==0 or i == a - 1:
                print(znak, end='')
            else:
                print(' ', end='')
            
        print()
    
        
def choinka1(h,znak):
    for i in range(h):
        print(znak,end='')
    print()
    
    
    
    
    
    
def choinka2(h,znak):
    
    




def main(args):
    a =int(input("Podaj 1 bok prostokata:"))
    b =int(input("Podaj 2 bok prostokata:"))
    znak =input("Podaj znak: ")
    znak2 =input("Podaj znak2: ")
    prostokat1(a, b ,znak)
    prostokat2(a, b ,znak)
    h =int(input("Podaj wysokosc choinki:"))
    znak =int(input("Podaj znak choinki:"))
    
    choinka1(h,znak)
    choinka2(h,znak)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
