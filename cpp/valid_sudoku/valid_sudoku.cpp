#include <iostream>
#include "valid_sudoku.hpp"

using namespace std;

int main(int argc, char* argv[]){
    ValidSudoku VS;
    int result;
    vector<vector<char>> testCase1 = {
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'}
    };

    result = VS.isValidSudoku(testCase1);

    cout << result << endl;
    return result;
}