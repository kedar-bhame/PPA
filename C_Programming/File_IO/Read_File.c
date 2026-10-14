#include<stdio.h>
#include<unistd.h>  
#include<io.h>          
#include<fcntl.h>       

int main()
{
    int fd = 0;
    char Arr[20] = {'\0'};
    fd = open("Hello.txt",O_RDONLY);

    if(fd == -1)
    {
        printf("Unable to open the file. \n");
        return -1;
    }
    else
    {
        printf("File gets opented with fd : %d\n",fd);  //
        read(fd,Arr,13);
        
        printf("Data from file is %s \n",Arr);

        close(fd);
    }

    return 0;
}