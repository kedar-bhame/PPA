#include<stdio.h>
#include<time.h>
int main(){
    clock_t start = clock();

    size_t n = 0;
    while(n < 1000000000){
        n++;
    }
    clock_t end = clock();
    double cpu_time_used =((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Execution time : %f seconds\n", cpu_time_used);
    return 0;
}