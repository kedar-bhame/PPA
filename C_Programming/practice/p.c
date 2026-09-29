#include<stdio.h>

int main()

{
    int  a= 10;
    int *p = &a;
    printf("%d, ",a);
    (*p) ++;
    printf("%d, ", a);
    
    return 0;
}