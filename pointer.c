#include<stdio.h>
int main(){
    printf("jay ganesh\n");
    int no = 11;
    int *p = &no;
    int **q = &p;
    int ***x = &q;
    int ****y = &x;
    int *****z = &y;
    printf("no = %d\n",no);
    printf("p = %d\n",p);
    printf("q = %d\n",q);
    printf("x = %d\n",x);
    printf("y = %d\n",y);
    printf("z = %d\n",z);
    printf("&no = %d\n",&no);

    printf("&p = %d\n",&p);
    printf("&q = %d\n",&q);
    printf("&x = %d\n",&x);
    printf("&y = %d\n",&y);
    printf("&z = %d\n",&z);

    printf("*p = %d\n",*p);
    printf("**x = %d\n",**x);
    printf("**y = %d\n",**y);
    printf("***z = %d\n",***z);

    printf("sizeof(no) = %d\n",sizeof(no));
    printf("sizeof(p) = %d\n",sizeof(p));
    printf("sizeof(*p) = %d\n",sizeof(*p));
    printf("sizeof(**q) = %d\n",sizeof(**q));
    printf("sizeof(***x) = %d\n",sizeof(***x));
    printf("sizeof(***y) = %d\n",sizeof(***y));
    printf("*****z = %d\n",*****z);
    printf("sizeof(*****z) = %d\n",sizeof(*****z));
    printf("&(**x) = %d\n",&(**x));
    printf("&(***y) = %d\n",&(***y));
    printf("****y = %d\n",****y);
    printf("***x = %d\n",***x);

    return 0;
}