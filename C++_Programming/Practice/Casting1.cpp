#include<iostream>
using namespace std;

class Base{
    public:
        int i,j;
};
class Derived : public Base{
    public:
        int x;
};

int main()
{
    Base* bobj = new Base;   // no casting
    Base* bobj1 = new Derived;  // up casting
    Derived* dobj = new Derived;    // no casting
    Derived* dobj1 = new Base;  // down casting not allowed
    cout<<sizeof(bobj)<<"\n";   // size of pointer is 4 bytes
    cout<<sizeof(bobj->i)<<"\n";
    cout<<sizeof(bobj->j)<<"\n";
    return 0;
}