#include<stdio.h>
int Addition(int a, int b){
    int Result = 0;
    Result = a + b;
    return Result;
}

int main()
{
    int x = 10, y = 12, Ans = 0;
    Ans = Addition(x,y);
    printf("Addition is : %d\n",Ans);

    return 0;
}