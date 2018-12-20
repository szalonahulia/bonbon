/*
 * petle_cw01.cpp

 */


#include <iostream>
using namespace std;

void cw_01() {
    int sum = 0;
    for(int i = 10; i <= 99; i += 2) {
        sum += i;
    }
    cout << sum;
}
void cw_02() {
    int a,b, parz=0,nieparz=0;
    cin>>a>>b;
    for(int i=a+1; i<b; i++)
    {
        if(i%2==0) parz+=i;
        else nieparz+=i;
    }
    cout<<parz-nieparz<<endl;
    system("pause");
    
}
void cw_03() {
    int liczba;
    int suma = 0;
    int podzielnych = 0;
    
    // wczytaj 8 liczb
    for(int i=0;i<8;++i)
    {
        cin >> liczba;
        suma += liczba;
        if(liczba % 5 == 0) podzielnych++;
    }
    
    cout << "Suma: " << suma << endl;
    cout << "Srednia: " << suma/8.0 << endl;
    cout << "Podzielnych przez 5: " << podzielnych << endl;
    
    cin.get();
    cin.ignore(1);
    


    
}
int main(int argc, char **argv)
{
	cw_01();
    cw_02();
    cw_03();
	return 0;
}

