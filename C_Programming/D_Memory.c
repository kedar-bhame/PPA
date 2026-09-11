#include<stdio.h>
#include<stdlib.h>


int main()
{
    int i = 10;
    printf("sizeof(i) = %zu \n",sizeof(i));
    printf("i = %d \n",i);

    int *P = NULL;

    P = (int *) malloc(5 * sizeof(int));

    printf("sizeof(P) = %zu \n",sizeof(P));
    printf("sizeof(*P) = %zu \n",sizeof(*P));
    printf("P = %d \n",P);
    printf("*P = %d \n",*P);
    P[0] = 11;
    P[1] = 21;
    P[2] = 51;
    P[3] = 61;
    P[4] = 71;
    P[5] = 81;
    printf("P[0] = %d \n",P[0]);
    printf("P[1] = %d \n",P[1]);
    printf("P[2] = %d \n",P[2]);
    printf("P[3] = %d \n",P[3]);
    printf("P[4] = %d \n",P[4]);
    printf("P[5] = %d \n",P[5]);

    printf("&P[0] = %d \n",&P[0]);
    printf("&P[1] = %d \n",&P[1]);
    printf("&P[2] = %d \n",&P[2]);
    printf("&P[3] = %d \n",&P[3]);
    printf("&P[4] = %d \n",&P[4]);
    printf("&P[5] = %d \n",&P[5]);
    return 0;
}