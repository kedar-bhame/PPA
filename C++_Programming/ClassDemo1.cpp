#include<iostream>
using namespace std;

class PPA
{
    public:
        int No1;
        int No2;

        void Display()
        {
            cout<<"Inside Display\n";
        }
};

int main()
{
    PPA pobj;

    cout<<sizeof(pobj)<<"\n";
    
    return 0;
}