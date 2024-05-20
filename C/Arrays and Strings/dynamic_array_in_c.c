/*
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/dynamic-array-in-c/problem
*/

#include <stdio.h>
#include <stdlib.h>

/*
 * This stores the total number of books in each shelf.
 */
int* total_number_of_books;

/*
 * This stores the total number of pages in each book of each shelf.
 * The rows represent the shelves and the columns represent the books.
 */
int** total_number_of_pages;

int main()
{
    int total_number_of_shelves;
    scanf("%d", &total_number_of_shelves);
    
    int total_number_of_queries;
    scanf("%d", &total_number_of_queries);
    
    total_number_of_books = (int*)calloc(total_number_of_shelves,  sizeof(int));            // Allocate memory for the books
    total_number_of_pages = (int**)calloc(total_number_of_shelves,  sizeof(int*));            // Allocate memory for the pages
    
    while (total_number_of_queries--) {
        int type_of_query;
        scanf("%d", &type_of_query);
        
        if (type_of_query == 1) {
            /*
             * Process the query of first type here.
             */
            int x, y;
            scanf("%d %d", &x, &y);
            total_number_of_books[x]++; // Increment the number of books in the xth shelf
            total_number_of_pages[x] = realloc(total_number_of_pages[x], sizeof(int*) * total_number_of_books[x]); // Create space on the shelf for the new book
            *(total_number_of_pages[x] + total_number_of_books[x] - 1) = y; // Change the number of pages of the last book on the xth shelf to y
            

        } else if (type_of_query == 2) {
            int x, y;
            scanf("%d %d", &x, &y);
            printf("%d\n", *(*(total_number_of_pages + x) + y));
        } else {
            int x;
            scanf("%d", &x);
            printf("%d\n", *(total_number_of_books + x));
        }
    }

    if (total_number_of_books) {
        free(total_number_of_books);
    }
    
    for (int i = 0; i < total_number_of_shelves; i++) {
        if (*(total_number_of_pages + i)) {
            free(*(total_number_of_pages + i));
        }
    }
    
    if (total_number_of_pages) {
        free(total_number_of_pages);
    }
    
    return 0;
}
