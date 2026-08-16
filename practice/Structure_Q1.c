// Student Structure in C: Input, display, and average marks calculation
#include<stdio.h>

struct student {
    char name[10];
    float marks;
};

int main(){

    int n;
    float sum, average;
    printf("Enter the no. of students info : ");
    scanf("%d",&n);

    struct student student[n];

    for(int i = 0 ; i < n; i++){
        printf("\nEnter the name of student %d: ", i+1);
        scanf("%s",&student[i].name);

        printf("\nEnter the marks for student %d: \n",i+1);
        scanf("%f",&student[i].marks);
    }


    for(int i = 0; i < n; i++){
        printf("Student %d name is : %s \n", i+1,student[i].name);
        printf("Student %d name is : %f \n", i+1,student[i].marks);
        sum += student[i].marks;
    }
    average = sum/n;
    printf("Average of all marks is : %f ",average);


    return 0;
}
