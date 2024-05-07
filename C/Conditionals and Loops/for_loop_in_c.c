/*
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/for-loop-in-c/problem
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
    char word_array[11][14] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "even", "odd"};
    for (int i = a; i <= b; i++) {
        if (i <= 9) {
            printf("%s\n", word_array[i-1]);
        }
        else if (i % 2 == 0) {
            printf("%s\n", word_array[9]);
        }
        else if (i % 2 != 0) {
            printf("%s\n", word_array[10]);
        }
    }

    return 0;
}

