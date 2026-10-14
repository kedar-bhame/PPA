#include<iostream>
using namespace std;

class base1
{
    public:
        int i;
        float f;
        virtual void gun() = 0;
        virtual void sun() = 0;
        virtual void run()          // 1000
        {        }
        
};

class base2
{
    public:
        int j;
        float g;
        virtual void mun() = 0;
        virtual void fun() = 0;
        void fun()          // 2000
        {        }
        
};

class derived : public base1,base2{
    public:
        int x;
        double d;
        void sun()
        {       }
        void fun()
        {       }
        void gun()
        {       }
        void mun()
        {        }

};

int main()
{
    derived dobj;
    // bp->fun();  // Base fun
    // bp->gun();  // Base gun
    // bp->sun();  // Derived sun
    // bp->run();  // Base run

    return 0;
}