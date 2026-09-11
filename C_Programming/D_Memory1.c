#include<stdio.h>
#include<stdlib.h>

int main()
{

        int i = 11;

        void *p = NULL;

        p =(int *) malloc(4*sizeof(int));
        *(int *)p = 12;

        printf("i = %d \n",i);
        printf("sizeof(i): %zu\n",sizeof(i));

        printf("p = %d \n",(int *)p);
        printf("sizeof(p): %zu\n",sizeof(p));

        printf("*p = %d \n",*(int *)p);
        printf("sizeof(*p): %zu\n",sizeof(*p));


    return 0;
}