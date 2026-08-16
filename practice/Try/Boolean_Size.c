#include<stdio.h>

struct Flags{
    unsigned long long int flag1 : 64;
    // unsigned char flag2 : 4;
    // unsigned char flag3 : 4;
};

int main(){

    struct Flags f = {18446744073709551617};

    printf("flag1 = %llu\n",f.flag1);
    // printf("flag2 = %u\n",f.flag2);
    // printf("flag3 = %u\n",f.flag3);

    printf("sizeof(f) : %d \n", sizeof(f));
    return 0;
}