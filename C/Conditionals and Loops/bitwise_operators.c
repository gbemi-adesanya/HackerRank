/*
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/bitwise-operators-in-c/problem
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int max (int array[]) {
    int max = array[0];
    for (int i = 1; i < 499500; i++) {
        if (array[i] > max) {
            max = array[i];
        }
    }
    return max;
}

void calculate_the_maximum(int n, int k) {  
  int and_array[499500] = {}, or_array[499500] = {}, xor_array[499500] = {};
  int index = 0;
  
  for (int i = 1; i <= n; i++) {
      for (int j = i+1; j <= n; j++) {
            int and_result = i&j;
            int or_result =  i|j;
            int xor_result = i^j;
        
            if (and_result < k) {
                and_array[index] = and_result;
            }
            if (or_result < k) {
                or_array[index] = or_result;
            }
            if (xor_result < k) {
                xor_array[index] = xor_result;
            }
        
            index++;
      }
    }
  
    int and_max = max(and_array);
    int or_max = max(or_array);
    int xor_max = max(xor_array);
    printf("%d\n%d\n%d\n", and_max, or_max, xor_max);
  }

  

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
