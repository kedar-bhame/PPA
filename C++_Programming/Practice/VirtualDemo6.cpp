#include<iostream>
using namespace std;

class Base
{
    public:
        int i, j;
        void fun()
        { cout<<"Base fun."<<"\n";}
        void gun()
        { cout<<"Base gun."<<"\n";}
        virtual void sun()
        { cout<<"Base sun."<<"\n";}
        virtual void run()
        { cout<<"Base run."<<"\n";}
};

class Derived : public Base{
    public:
        int x;
        void fun()
        { cout<<"Derived fun"<<"\n"; }
        void sun()
        { cout<<"Derived sun"<<"\n"; }
        void mun()
        { cout<<"Derived mun"<<"\n"; }
        void bun()
        { cout<<"Derived bun"<<"\n"; }

};

int main()
{
    Base * bp = new Derived();
    bp->fun();  // Base fun
    bp->gun();  // Base gun
    bp->sun();  // Derived sun
    bp->run();  // Base run

    return 0;
}