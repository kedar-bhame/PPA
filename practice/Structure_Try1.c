#include<stdio.h>

#pragma pack(1)
struct Demo{
    int i;     // 4 bytes
    float f;    // 4 bytes
    char ch;    // 4 bytes or in pragma pa ch(1) than 1 byte
    struct Demo *p;     // 8 bytes but here is 4 bytes
};

int main(){
    // printf("Jay Ganesh...\n");
    struct Demo dobj;
    printf("sizeof(dobj) : %d \n",sizeof(dobj));
    printf("sizeof(dobj.i) : %d \n",sizeof(dobj.i));
    printf("sizeof(dobj.f) : %d \n",sizeof(dobj.f));
    printf("sizeof(dobj.ch) : %d \n",sizeof(dobj.ch)); 
    // printf("dobj.ch+1 : %d \n",*(&dobj.ch+1));
    // printf("dobj.ch+2 : %d \n",*(&dobj.ch+2));
    // printf("dobj.ch+3 : %d \n",*(&dobj.ch+3));
    // printf("dobj.ch+4 : %d \n",*(&dobj.ch+4));
    printf("sizeof(dobj.p) : %d \n",sizeof(dobj.p));
    return 0;
}