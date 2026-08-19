#include<stdio.h>

int main(){
    char ch = 'A';
    int no = 11;
    float Marks = 90.78f;
    double d = 90.56789;

    char *cp = &ch;
    int *ip = &no;
    float *fp = &Marks;
    double *dp = &d;

    printf("cp = %d\n",sizeof(cp));
    printf("*cp = %d\n",sizeof(*cp));
    printf("ch = %d\n",sizeof(ch));

    return 0;
}