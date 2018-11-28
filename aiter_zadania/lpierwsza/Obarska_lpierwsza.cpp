/*
 * Obarska_lpierwsza.cpp
 * 

 */


#include <iostream>
using namespace std;
#include <cstdlib>
bool czy_pierwsza(int n)
{   
        if(n < 2)
                return false; 
        for(int i = 2 ; i * i <= n ; i++)
                if (n % i == 0)
                        return false;
        return true;
    
    
    
    
}
int main(int argc, char **argv)
{
	int n;
    cout << "Podaj liczbę: ";
    cin >> n;
    if(czy_pierwsza(n))
            cout << "Liczba " "<<n<<"
            cout << "Liczba " "<<n<<"
    system("pause");
	return 0;
}

