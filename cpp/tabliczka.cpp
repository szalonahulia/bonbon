/*
 * tabliczkacpp.cxx
 * 
 * Copyright 2018  <>
 */


#include <iostream>

using namespace std;

void tabliczka(int x, int y) {
    for (int i = 1; i <= x; i ++) {
        for (int j = 1; j <= y; i++) {
            cout << 1 * j << ' ';
        }
    }
}

int main(int argc, char **argv)
{   
    int m;
	m = 0; //inicjacja
    
    
    int n = 0;
    
    cout << "Podaj 1. liczbe: ";
    cin >> m;
    cout << "Podaj 2.liczbe: ";
    cin >> n;
    tabliczka(m, n);
    
	return 0;
}

