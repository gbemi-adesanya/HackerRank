/*
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/sum-numbers-c/problem
*/

#include <stdio.h>

int main()
{
	  int first_int, second_int;
    float first_float, second_float;
    scanf("%d %d\n", &first_int, &second_int);
    scanf("%f %f", &first_float, &second_float);
    
    printf("%d %d\n", first_int + second_int, first_int - second_int);
    printf("%.1f %.1f", first_float + second_float, first_float - second_float);
    return 0;
}
