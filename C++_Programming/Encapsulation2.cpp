#include<iostream>
using namespace std;

#pragma pack(1)
class Demo
{
    int i ;
    char ch;
    float f;

};

int main()
{
    Demo dobj;
    cout<<sizeof(dobj)<<"\n";
    return 0;
}