#include<iostream>
#include<algorithm>
using namespace std;

class Solution {
public:
    bool bitmap[28];
    int max_length = 1;
    int length = 1;

    int lengthOfLongestSubstring(string s) {
	int string_length =  s.length();
        for (int i = 0; i < string_length; i++)
        {
            if (length > max_length)
            {
                max_length = length;
            }
	    //To initialise an array
            fill_n(bitmap, 28,0);
            bitmap[97-s.at(i)] = 1;
            length = 1;

            for (int j = i+1; j < string_length; j++)
            {
                if (bitmap[97-s.at(j)] == 0)
                {
                    bitmap[97-s.at(j)] = 1;
                    length++;
                }
                else 
                {
                    break;
                }
            }
        }
        return max_length;
    }    
};


int main()
{
	Solution s;
	int length = s.lengthOfLongestSubstring("aw");
	cout << length << endl;
}
