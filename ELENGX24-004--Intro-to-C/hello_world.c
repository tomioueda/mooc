#include <stdio.h>

int main(void) {
    int num;
    printf("Hello world! Give me an integer:\n");
    scanf("%d", &num);
    printf("Thanks! I've always been fond of %d.\n", num);
    return 0;
}