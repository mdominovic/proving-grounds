#include <iostream>
#include "reverse_integer.hpp"

using namespace std;

int main(int argc, char* argv[]){
    ReverseInteger ri;
    int a = 0;
    // cout << argv[1]  << endl;
    if (argc == 2)
    {
        a = atoi(argv[1]);
    }

    cout << a << endl;
    cout << ri.reverse(a) << endl;
    return ri.reverse(a);
}