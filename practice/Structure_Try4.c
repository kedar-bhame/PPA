#include<stdio.h>

#pragma pack(1)
struct Demo {
    int i;
    char ch;
    struct Inside {
        int a;
        char ich;
    }iobj;
};

int main(){

    struct Demo dobj;

    printf("sizeof(dobj) : %d \n",sizeof(dobj));
    printf("sizeof(dobj.i) : %d \n",sizeof(dobj.i));
    printf("sizeof(dobj.ch) : %d \n",sizeof(dobj.ch));
    printf("sizeof(dobj.iboj.a) : %d\n", sizeof(dobj.iobj.a));
    printf("sizeof(dobj.iboj.ich) : %d \n",sizeof(dobj.iobj.ich));

    return 0;
}