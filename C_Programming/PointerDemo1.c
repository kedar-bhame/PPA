#include<stdio.h>

int main(){
    char ch = 'A';
    int no = 11;
    float Marks = 90.78f;
    double d = 90.56789;

    printf("sizeof ch : %d\n",sizeof(ch));
    printf("sizeof no : %d\n",sizeof(no));
    printf("sizeof Marks : %d\n",sizeof(Marks));
    printf("sizeof d : %d\n",sizeof(d));
    return 0;
}