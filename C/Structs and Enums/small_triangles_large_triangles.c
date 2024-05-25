/*
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/small-triangles-large-triangles/problem
*/


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

double delta (triangle tr) {
    double p = (tr.a + tr.b + tr.c) / 2.0;
    double area__ = p * (p - tr.a) * (p - tr.b) * (p - tr.c);
    return sqrt(area__);
}

int comparator (const void *a, const void *b) {
    triangle *t1 = (triangle*) a, *t2 = (triangle*) b;
    double area1 = delta(*t1), area2 = delta(*t2);   
    if (area1 > area2) {
        return 1;
    } else if (area1 < area2) {
        return -1;
    } else {
        return 0;
    }
}

void sort_by_area(triangle* tr, int n) {
    qsort(tr, n, sizeof(triangle), comparator);
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
