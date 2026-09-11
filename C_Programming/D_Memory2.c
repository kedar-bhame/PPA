#include<stdio.h>
#include<stdlib.h>

int main()
{

        int *p= NULL;
        p = malloc(4 * sizeof(int));

        printf("p = %d \n",p);
        printf("sizeof(p): %zu\n",sizeof(p));

        printf("*p = %d \n",*p);
        printf("sizeof(*p): %zu\n",sizeof(*p));

        free(p);

    return 0;
}