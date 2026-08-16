#include<stdio.h>

#pragma pack(1)
struct Demo{
    int i;     
    struct Demo *p;     
};

int main(){
   
    struct Demo dobj1, dobj2, dobj3, *dp;
    dp = &dobj1;

    dobj1.i = 10;
    dobj2.i = 20;
    dobj3.i = 30;

    dobj1.p = &dobj2;
    dobj2.p = &dobj3;
    dobj3.p = NULL;

    printf("dobj1.i : %d\n", dobj1.i);
    printf("dobj1.p -> i : %d\n", dobj1.p -> i);
    printf("dobj1.p -> p -> i : %d\n", dobj1.p -> p -> i);



    printf("sizeof(dobj) : %d \n",sizeof(dobj1));

    printf("sizeof(dobj.i) : %d \n",sizeof(dobj1.i));      
    printf("sizeof(dobj.p) : %d \n",sizeof(dobj1.p));
    return 0;
}