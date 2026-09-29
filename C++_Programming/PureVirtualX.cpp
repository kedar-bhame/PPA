#include<iostream>
using namespace std;

#pragma pack(1)
class Base
{
    public:
        int i, j;

        int Addition(int no1, int no2)  // 1000
        {
            return no1 + no2;
        }
        virtual int Substraction(int no1, int no2) = 0; //--------
};

#pragma pack(1)
class Derived : public Base
{
    public:
        int x;
        int Substraction(int no1, int no2)  // 2000
        {
            return no1 - no2;
        }
        int Multiplication(int no1, int no2)    // 3000
        {
            return no1 * no2;
        }
};

int main()
{
    Derived dobj;
    int Ret = 0;
    
    cout<<"sizeof Base class is : "<<sizeof(Base)<<"\n";    //12 pointer is 4 byte
    cout<<"sizeof Derived class is : "<<sizeof(Derived)<<"\n";  //16 pointer is 4 byte

    Ret = dobj.Addition(11,10);
    cout<<"Addition is : "<<Ret<<"\n";

    Ret = dobj.Substraction(11,10);
    cout<<"Substraction is : "<<Ret<<"\n";

    Ret = dobj.Multiplication(11,10);
    cout<<"Multiplication is : "<<Ret<<"\n";

    return 0;
}