#include <iostream>
#include <vector>
#include <iterator>
#include <set>

using namespace std;

class TwoSum
{
public:
    vector<int> twoSum(vector<int> &numberSet, int result)
    {
        vector<int> numbers_position;

        for (unsigned int i = 0; i < numberSet.size() - 2; i++)
        {
            for (unsigned int j = i + 1; j < numberSet.size()-1; j++)
            {
                if (numberSet[i] + numberSet[j] == result)
                {
                    numbers_position.push_back(i);
                    numbers_position.push_back(j);
                }
            }
        }
        return numbers_position;
    }
};