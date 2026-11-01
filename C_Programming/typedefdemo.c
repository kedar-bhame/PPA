#include<stdio.h>
typedef unsigned int UINT;
typedef unsigned long int ULONG;

int main()
{
    UINT i = 11;    // unsigned int i = 11;
    ULONG j = 51;   // unsigned long int j = 51;

    printf("Inside typedef demo\n");
    printf("%d\n",sizeof(i));
    printf("%d\n",sizeof(j));

    return 0;
}