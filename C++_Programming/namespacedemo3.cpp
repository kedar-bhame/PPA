#include<iostream>
using namespace std;

namespace Marvellous
{
    int i = 11;

    void Display()
    {
        cout<<"Inside Display\n";
    }
}
int main()
{
    cout<<Marvellous::i<<"\n";

    Marvellous::Display();

    return 0;
}