#include<stdio.h>
#include<unistd.h>  
#include<io.h>          
#include<fcntl.h>       

int main()
{
    int fd = 0;
    char Arr[] = "Marvellous Infosystems";
    fd = open("Hello.txt",O_RDWR | O_APPEND);

    if(fd == -1)
    {
        printf("Unable to open the file. \n");
        return -1;
    }
    else
    {
        printf("File gets opented with fd : %d\n",fd);  //
        write(fd,Arr,10);
        
        close(fd);
    }

    return 0;
}