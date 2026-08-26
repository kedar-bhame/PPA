#include<iostream>
using namespace std;

class Arithematic
{
    public:
        int No1;
        int No2;
        
        Arithematic()
        {
            No1 = 0;
            No2 = 0;
        }

        Arithematic(int i, int j)
        {
            No1 = i;
            No2 = j;
        }
};

int main()
{
    Arithematic aobj1;
    Arithematic aobj2(10,11);

    cout<<aobj1.No1<<"\n";
    cout<<aobj1.No2<<"\n";

    cout<<aobj2.No1<<"\n";
    cout<<aobj2.No2<<"\n";

    return 0;
}