/*
Difficulty: hard
Problem: https://www.hackerrank.com/challenges/sorting-array-of-strings/problem
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lexicographic_sort(const char* a, const char* b) {
    return strcmp(a, b);
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    return strcmp(b, a);
}

int distinct_characters(const char* string) {
    int count[26] = {0}; // Initialize array for each letter
    int distinct = 0;
    
    while (*string) {
        if (count[*string - 'a'] == 0) {
            /*
            If the letter has never been encountered e.g.
            If *string is 'b', 'b' - 'a' = 1, so the index at 1 (the 2nd element) is updated.
            If *string is 'y', 'y' - 'a' = 24, so the index at 24 (the 25th element) is updated
            */
            distinct++;
        }
        count[*string - 'a']++; // Update the letter count after encountering
        string++;
    }
    return distinct;
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int a_count = distinct_characters(a);
    int b_count = distinct_characters(b);
    
    if (a_count == b_count) {
        return strcmp(a, b);
    }
    return a_count - b_count;
}

int sort_by_length(const char* a, const char* b) {
    int a_len = strlen(a), b_len = strlen(b);
    if (a_len == b_len) {
        return strcmp(a, b);
    }
    return a_len - b_len;
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
    // bubble sort
    for (int i = 0; i < len; i++) {
        for (int j = i + 1; j < len; j++) {
            if (cmp_func(arr[i], arr[j]) > 0) {
                char* temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}


int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }
  
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}
