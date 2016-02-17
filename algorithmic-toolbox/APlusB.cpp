/*
APlusB.cpp
By Tomio Ueda

Problem. Given two digits a and b, find a+b.

Input format. The first line of the input contains two integers a and b (separated by a space).
Constraints. 0≤a,b≤9.
Output format. Output a+b.
*/

#include <iostream>

int main()
{
    int a;
    int b;
    int sum;
    
    std::cin >> a >> b;
    sum = a + b;
    
    if ((a >= 0) && (b <= 9))
    {
        std::cout << sum;
        return 0;
    }
    else
    {
        return 1;
    }
}
