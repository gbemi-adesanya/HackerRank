/*
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/printing-pattern-2/problem
*/

#include <stdio.h>

int main() 
{

    int n;
    scanf("%d", &n);

    int length = 2*n - 1;
    for (int row = 0; row < length; row++) {
        for (int col = 0; col < length; col++) {
            int min = row < col ? row : col;
            /*   if row < col, min = row
                 if row > col, min = col  */

            int bottom = length - row;
            int right = length - col;
            min = min < bottom ? min : bottom - 1;
            /*   if min < bottom, min = min
                 if min > bottom, min = bottom - 1  */

            min = min < right ? min : right - 1;
            /*   if min < right, min = min
                 if min > right, min = right - 1  */
            printf("%d ", n - min);
        }
        printf("\n");
    }
    return 0;
}
