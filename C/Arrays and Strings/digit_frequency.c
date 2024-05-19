/*
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/frequency-of-digits-1/problem
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {

    char s[1000];
    scanf("%s", s);
    int* arr = calloc(10, sizeof(int));

    for (int i = 0; i < strlen(s); i++) {        
        switch (s[i]) {
            case '0':
                *arr += 1;
                continue;;
            case '1':
                arr[1]++;
                continue;
            case '2':
                arr[2]++;
                continue;
            case '3':
                arr[3]++;
                continue;
            case '4':
                arr[4]++;
                continue;
            case '5':
                arr[5]++;
                continue;
            case '6':
                arr[6]++;
                continue;
            case '7':
                arr[7]++;
                continue;
            case '8':
                arr[8]++;
                continue;
            case '9':
                arr[9]++;
                continue;
            default:
                continue;
        }
        
    }
    
    for (int i = 0; i < 10; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}
