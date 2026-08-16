#include<stdio.h>
int main(){
    float f[2];
    int arr[4];
    for(int i = 0; i < 4; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
    char carr[4];
    int iarr[4];
    float farr[4];
    double darr[4];
    printf("\n arr : %d\n",arr);
    printf(" &arr : %d\n",&arr);
    printf(" arr[0] : %d\n",arr[0]);
    printf(" &arr[0] : %d\n",&arr[0]);
    printf("size of carr : %d\n",sizeof(carr));
    printf("size of iarr : %d\n",sizeof(iarr));
    printf("size of &iarr : %d\n",&iarr);

    printf("size of &iarr+1 : %d\n",&iarr+1);

    printf("size of farr : %d\n",sizeof(farr));
    printf("size of darr : %d\n",sizeof(darr));


    // printf(" arr++ : %d\n",arr++);
    // printf(" &arr++ : %d\n",&arr++);
    // printf(" arr[0]++ : %d\n",arr[0]++);
    // printf(" &arr[0]++ : %d\n",&arr[0])++);

    

    return 0;
}