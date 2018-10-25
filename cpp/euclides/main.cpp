#include <iostream>

using namespace std;
int nwd_klasyczne(int a , int b) {
    while(a !=b){
        if(a > b)
            a = a - b;
        else
            b = - a;
    }
    return a;
}
int nwd_optymalny(int a, int b) {
    while( a > 0) {
    it(a > 0) {
    a = a% b;
    b = b- a;
    }
    else
    cout << b;
    }
}
int main()
{
    int a,b;
    a = b = 0;
    cout <<"Podaj 2 liczby: ";
    cin >> a >> b;
    cout << "nwd(" << a << " , " << b << ") = "
        << nwd_klasyczne(a,b) << endl;

    return 0;
}
