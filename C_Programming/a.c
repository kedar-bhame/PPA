#include<stdio.h>

int main(){
    signed char ch1 = 97;
    unsigned char uch2 = 97;
    printf("ch1  is : %c & %d \n",ch1,ch1);
    printf("ch1 size is : %c & %d \n",sizeof(ch1),sizeof(ch1));

    printf("uch2  is : %c & %d  \n",uch2,uch2);
    printf("uch2 size is : %c & %d \n",sizeof(uch2),sizeof(uch2));


    return 0;
}