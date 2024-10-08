/*
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/recursion-in-c/problem
*/

#include <stdio.h>

int find_nth_term(int n, int a, int b, int c) {
  int ans;
  if (n == 1) {
      ans = a;
  } else if (n == 2) {
      ans = b;
  } else if (n == 3) {
      ans = c;
  } else {
      ans = find_nth_term(n-1, a, b, c) + find_nth_term(n-2, a, b, c) + find_nth_term(n-3, a, b, c);
  }
  
  return ans;
  }


int main() {
    int n, a, b, c;
  
    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);
 
    printf("%d", ans); 
    return 0;
}
