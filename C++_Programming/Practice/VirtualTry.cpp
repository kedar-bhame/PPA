#include<iostream>
using namespace std;

class base
{
    public:
        int i;
        float f;

        void fun()          // 1000
        { cout<<"Inside base fun."<<"\n";  }
        virtual void gun()      //2000
        {  cout<<"Inside base gun."<<"\n"; }
};
class derived : public base
{
    public :
        int i;
        double d;

        virtual void fun()     //3000
        {  cout<<"Inside derived fun."<<"\n"; } 
        void gun()          // 4000
        {  cout<<"Inside derived gun."<<"\n"; }  
        virtual void sun()      //5000
        {  cout<<"Inside derived sun."<<"\n"; }
};

int main()
{
    derived dobj;
    dobj.fun();     //3000
    dobj.gun();     //4000
    dobj.sun();     //5000

    return 0;
}