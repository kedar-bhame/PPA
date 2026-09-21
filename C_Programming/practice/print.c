#include<stdio.h>

int main()
{
    char str[] = "Hello %d %d \n";
    // printf("Hello %d \n", no);
    int no = 5;
    int no1 = 10;
    int no2 = 20;

    printf(str,no1);
    
    return 0;
}