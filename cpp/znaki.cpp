/*
 * znaki.cpp
 * 
 * Copyright 2018  <>
 
 */


#include <iostream>
using namespace std;
int zlicz(char tab[]) {
    int i = 0; 
    while (tab[i] != '\0') i++;
    return i;
}
void drukuj(char tab[], int roz) {
    
    for(int i=0; i<roz; i++) {
        cout << tab[i] << " ";
    
    }
}
void liczznaki(char tab[], int roz) {
    int spacje = 0;
    int interpunkcja = 0;
    int symbole = 0;
    for (int i = 0; i<roz; i++) {
        if (tab[i] == ' ') spacje++;
        else if (tab[i] == '.' || tab[i] == ',')
            interpunkcja++;
        else if (tab[i] == '(' || tab[i] == ')') symbole++;
    }
}

int main(int argc, char **argv)
{
    const int rozmiar = 20;
    char tab[rozmiar];
    cout << "Jak sie nazywasz?" << endl;
    //cin >> tab;
    cin.getline(tab, rozmiar);
    //cout << "Czesc " << tab << "!" << endl;
    drukuj(tab, zlicz(tab));
    
    return 0;
}

