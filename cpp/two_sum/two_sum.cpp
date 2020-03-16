#include <iostream>
#include <set>
#include "two_sum.hpp"
#include <vector>

using namespace std;

int main(int argc, char* argv[]){
    TwoSum TS;
    vector<int> numbers;
    int result = atoi(argv[argc-1]);
    for(int i=1;i<=argc-1;i++){
        numbers.push_back(atoi(argv[i]));
    }
    numbers.pop_back();
    vector<int> func_result = TS.twoSum(numbers,result);

    return 0;
}