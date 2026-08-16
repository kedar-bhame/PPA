#include<stdio.h>

#pragma pack(1)
struct Demo{
    int i; 
    int j;
    int k;    
    float f; 
    char ch; 
};

int main(){
   
    struct Demo dobj1,dobj2,dobj3;
    dobj1.i = 10;
    dobj1.j = 20;
    
    struct Demo * Arr[3] = {&dobj1,&dobj2,&dobj3};

    printf("%d",(dobj1));

    return 0;
}