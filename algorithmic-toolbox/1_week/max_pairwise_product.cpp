/*
max_pairwise_product.cpp
By Tomio Ueda

Problem: Given a sequence of non-negative integers a0,…,an−1, 
find the maximum pairwise product, that is, the largest integer 
that can be obtained by multiplying two different elements from 
the sequence.

Input format:
The first line of the input contains an integer n. 
The next line contains n non-negative integers a0,…,an−1 
(separated by spaces).

Constraints:
2≤n≤2⋅105; 0≤a0,…,an−1≤105.

Output format:
Output a single number — the maximum pairwise product.
*/

#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;

int MaxPairwiseProduct(const vector<int>& numbers) {
  int result = 0;
  int n = numbers.size();
  for (int i = 0; i < n; ++i) {
    for (int j = i + 1; j < n; ++j) {
      if (numbers[i] * numbers[j] > result) {
        result = numbers[i] * numbers[j];
      }
    }
  }
  return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }

    int result = MaxPairwiseProduct(numbers);
    cout << result << "\n";
    return 0;
}

