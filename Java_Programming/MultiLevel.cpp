#include<iostream>
using namespace std;
class Base
{
    public:
    int i,j;
    Base()
    {
        cout<<"Inside Base Constructor.\n";
    }
    ~Base()
    {
        cout<<"Inside Base Destructor.\n";
    }
    void fun()
    {
        cout<<"Inside Base fun\n";
    }
    void gun()
    {
        cout<<"Inside Base gun\n";
    }
};

class Derived : public Base
{
    public:
        int x,y;
        Derived()
        {
            cout<<"Inside Derived Constructor.\n";
        }
        ~Derived()
        {
            cout<<"Inside Derived Destructor.\n";
        }
        void sun()
        {
            cout<<"Inside Derived sun\n";
        }
};

class DerivedX : public Derived
{
    public:
    int a;
    DerivedX()
    {
        cout<<"Inside DerivedX Constructor\n";
    }
    ~DerivedX()
    {
        cout<<"Inside DerivedX Destructor\n";
    }
    void run()
    {
        cout<<"Inside DerivedX run\n";
    }
};

int main()
{
    DerivedX dobj;
    dobj.fun();
    dobj.gun();
    dobj.sun();
    dobj.run();
    return 0;
}