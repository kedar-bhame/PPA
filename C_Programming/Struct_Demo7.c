#include<stdio.h>

#pragma pack(1)
struct Demo{
    int no;
    int Arr[3];
};

int main(){

    struct Demo dobj;

    printf("%d\n",sizeof(dobj));  //16 bytes

    dobj.no = 10;

    dobj.Arr[0] = 11;
    dobj.Arr[1] = 21;
    dobj.Arr[2] = 51;

    printf("%d\n",dobj.Arr[1]);

    return 0;
}