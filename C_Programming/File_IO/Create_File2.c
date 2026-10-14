#include<stdio.h>
#include<unistd.h>  //
#include<io.h>          // any one for creat
#include<fcntl.h>       //

int main()
{
    int fd = 0;

    fd = creat("Hello.txt",0777);

    if(fd == -1)
    {
        printf("Unable to create the file. \n");
        return -1;
    }
    else
    {
        printf("File gets created with fd : %d\n",fd);  // 3
    }

    return 0;
}