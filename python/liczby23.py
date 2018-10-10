#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby23.py
def liczby2():
    """
    funkcja drukuje wszytskiie liczby 2-cyfrowe,w ktorych nie powtarzaja sie cyfyr.Na koniec zwraca ilosc takich liczb.
    Wyklucza liczby: 11,22,33 itd.

    """
    ile = 0
    for i in range(1, 10):
        for j in range(10):
            if i != j:
                print("{}{} ".format(i, j), end="")
                ile = ile +1
    return ile 

def main(args):
    print(" Liczb 2-cyfrowych:", liczby2())

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
