/*
 * liczba23.cxx
 */


#include <iostream>
using namespace std;
int liczby2() {
    int ile = 0;
    for (int i = 1; 1 < 10; i++) {
        for(int j = 1; 1 < 10; j++) {
            if(i != j) {
                cout << i << j << "";
                ile++;
            }
        }
    }
    return ile;
}
int main(int argc, char **argv)
{   cout << "\n\nliczb2 cyfrowych:" , liczby 2();
	
	return 0;
}

