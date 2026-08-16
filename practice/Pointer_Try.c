#include<stdio.h>

int main(){

    float a = 61.17;

    void *p = &a;

    void **q = &p;

    void ***r = &q;

    printf("a : %f \n",a);
    printf("*p : %f \n", *(float *)p);
    printf("**q : %f \n", (float *)*(void **)*q);
    printf("***r : %f \n",(float *)*(void ***)*(void **)*r);
    

     
    return 0;
}