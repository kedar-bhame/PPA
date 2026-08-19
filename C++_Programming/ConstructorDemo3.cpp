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

        // Parameterised Constructor
        PPA(int a, int b)
        {
            cout<<"Inside Parameterised Constructor\n";
        }

        // Copy Constructor
        PPA(PPA &obj)
        {
            cout<<"Inside Copy Constructor\n";
        }

        ~PPA()
        {
            cout<<"Inside Destructor\n";
        }

};

int main()
{
    PPA pobj1;      // Default
    PPA pobj2(11, 21);      // Parameterised
    PPA pobj3(pobj1);       // Copy

    return 0;
}