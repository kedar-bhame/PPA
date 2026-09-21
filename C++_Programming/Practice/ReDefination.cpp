#include<iostream>
using namespace std;

class Base{
    public:
        void fun(){
            cout<<"Inside fun of Base."<<"\n";
        }
};
class Derived : public Base{
    public:
        void fun(){
            cout<<"Inside fun of Base."<<"\n";
        }
};

int main()
{
    Base* bobj = new Base;   // no casting
    Base* bobj1 = new Derived;  // up casting
    Derived* dobj = new Derived;    // no casting
    // Derived* dobj1 = new Base;  // down casting not allowed
    bobj->fun();
    bobj1->fun();
    dobj->fun();
    return 0;
}