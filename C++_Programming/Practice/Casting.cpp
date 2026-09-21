#include<iostream>
using namespace std;

int main()
{
    char ch = 'K';
    int no = 21;

    char *cp = NULL;
    int *ip = NULL;

    cp = &ch;   //no casting
    ip = &no;   //no casting

    cp = &no;   // up casting
    ip = &ch;   //down casting
    return 0;
}