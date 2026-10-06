#include<iostream>
using namespace std;

class base
{
    public:
        int i;
        float f;

        virtual void fun()      // 1000
        { cout<<"Inside base fun."<<"\n";  }
        virtual void gun()      //2000
        {  cout<<"Inside base gun."<<"\n"; }
        virtual void sun()      //3000
        {  cout<<"Inside base sun."<<"\n"; }
        void run()              //4000
        {  cout<<"Inside base run."<<"\n"; }
};
class derived : public base
{
    public :
        int i;
        double d;

        virtual void fun()      //5000
        {  cout<<"Inside derived fun."<<"\n"; } 
        virtual void gun()      //6000
        {  cout<<"Inside derived gun."<<"\n"; }  
        void sun()              //7000
        {  cout<<"Inside derived sun."<<"\n"; }
        virtual void run()      //8000
        {  cout<<"Inside derived run."<<"\n"; }
};

int main()
{   
    base *bobj = new derived();
    // derived dobj;
    bobj->fun();     //5000     derived
    bobj->gun();     //6000     derived
    bobj->sun();     //7000     derived
    bobj->run();     //4000     base

    return 0;
}