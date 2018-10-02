#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  PETLE.CW5.py
#  
#  


def main(args):
    for liczba in range(10,100):
        # ~if liczba % 2 == 0: #Czy parzysta
            # ~if liczba % 3 == 0: #czy liczba podzielna prezez 3
                # ~print(licba, "" , end"")
        if liczba % 6 == 0:
            print(liczba,"",end="")
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
