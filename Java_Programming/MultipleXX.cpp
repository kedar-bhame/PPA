#include<iostream>
using namespace std;

class BaseA
{
    public:
        int i,j;

        BaseA()
        {
            cout<<"Inside BaseA constructor\n";
        }
        ~BaseA()
        {
            cout<<"Inside BaseA Destructor\n";
        }
        void fun()
        {
            cout<<"Inside BaseA fun\n";
        }
};

class BaseB
{
    public:
        int x,y;

        BaseB()
        {
            cout<<"Inside BaseB constructor\n";
        }
        ~BaseB()
        {
            cout<<"Inside BaseB Destructor\n";
        }
        void gun()
        {
            cout<<"Inside BaseB fun\n";
        }
};

class Derived : public BaseB, public BaseA
{
    public:
        int a;

        Derived()
        {
            cout<<"Inside Derived constructor\n";
        }
        ~Derived()
        {
            cout<<"Inside Derived Destructor\n";
        }
        void sun()
        {
            cout<<"Inside Derived sun\n";
        }
};
int main()
{
    Derived dobj;
    dobj.fun();
    dobj.gun();
    dobj.sun();
    return 0;
}