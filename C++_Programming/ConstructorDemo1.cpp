#include<iostream>
using namespace std;

class PPA
{
    public:
        int No1;
        int No2;

        // Default Constructor
        PPA()
        {
            cout<<"Inside Default Constructor\n";
        }

        ~PPA()
        {
            cout<<"Inside Destructor\n";
        }

};

int main()
{
    PPA pobj1;
    PPA pobj1;

    return 0;
}