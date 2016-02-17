"""
max_pairwise_product.py
By Tomio Ueda

Problem
Given a sequence of non-negative integers a0,…,an−1, 
find the maximum pairwise product, that is, the largest 
integer that can be obtained by multiplying two different 
elements from the sequence.

Input format:
The first line of the input contains an integer n. 
The next line contains n non-negative integers a0,…,an−1 
(separated by spaces).

Constraints:
2 <= n <= 2 * 105; 
0≤a[0],…,a[n−1]≤10^5

Output format:
Output a single number — the maximum pairwise product.
"""

if __name__ == '__main__':

    list_size = int(input())
    input_numbers = [int(x) for x in input().split()]
    assert(len(input_numbers) == list_size)

    result = 0

    for i in range(0, list_size):
        for j in range(i+1, list_size):
            if input_numbers[i]*input_numbers[j] > result:
                result = input_numbers[i]*input_numbers[j]

    print(result)