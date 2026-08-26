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

        int Addition()
        {
            int Ans = 0;
            Ans = No1 + No2;
            return Ans;
        }
};

int main()
{
    Arithematic aobj1(10,11);
    int Result = 0;

    Result = aobj1.Addition();

    cout<<"Addition is : "<<Result<<"\n";    

    return 0;
}