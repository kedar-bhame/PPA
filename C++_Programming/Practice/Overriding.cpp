#include<iostream>
using namespace std;

class Base{
    public:
        int i, j;
         void fun(){
            cout<<"Inside fun of Base."<<"\n";
        }
};
class Derived : public Base{
    public:
        int x;
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
    cout<<"sizeof(Base)"<<sizeof(Base)<<"\n";
    cout<<"sizeof(bobj) "<<sizeof(bobj)<<"\n";   // size of pointer is 4 bytes
   
    cout<<"sizeof(Derived)"<<sizeof(Derived)<<"\n";
    cout<<"sizeof(bobj1) "<<sizeof(bobj)<<"\n";   // size of pointer is 4 bytes

    return 0;
}