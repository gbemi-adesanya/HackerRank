/*
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/1d-arrays-in-c/problem
*/

// Didn't allocate space to an array using malloc()

#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int sum = 0;
    for (int i = 0;  i < n; i++) {
        int num;
        scanf("%d", &num);
        sum += num;
    }
    printf("%d", sum); 
    return 0;
}
