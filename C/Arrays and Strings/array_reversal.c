/*
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/reverse-array-c/problem
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }


    /* Write the logic to reverse the array. */
    for(i = num - 1; i >= 0; i--)
        // Start from the element at the last index (num - 1) and work until the first element (0)
        printf("%d ", *(arr + i));
        
    free(arr);
    return 0;
}
