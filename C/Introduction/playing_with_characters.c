/*
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/playing-with-characters/problem
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char ch;
    int width = 100;
    char s[width];
    char sen[width];
    
    scanf("%c", &ch);
    scanf("%s\n", &s);
    scanf("%[^\n]%*c", &sen);
    
    printf("%c\n%s\n%s", ch, s, sen);  
    return 0;
}
