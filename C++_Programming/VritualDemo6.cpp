#include<iostream>
using namespace std;
#pragma pack(1)
class Base
{
    public:
    int i, j;
    void fun()                      // 1000
    {   cout<<"Base fun"<<"\n";  }
    void gun()                      // 2000
    {   cout<<"Base gun"<<"\n";   }
    virtual void sun()              // 3000
    {   cout<<"Base sun"<<"\n";   }
    virtual void run()              // 4000
    {   cout<<"Base run"<<"\n";   }
};  // 16 bytes if pointer is 8 bytes

#pragma pack(1)
class Derived : public Base
{
    public:
    int x;
    void fun()                          // 5000
    {   cout<<"Derived fun"<<"\n";  }
    void sun()                          // 6000
    {   cout<<"Derived sun"<<"\n";   }
    virtual void mun()                  // 7000
    {   cout<<"Derived mun"<<"\n";   }
    virtual void bun()                  // 8000
    {   cout<<"Derived bun"<<"\n";   }
};  // 20 bytes if pointer is 8 bytes

int main()
{
    Base * bp = new Derived();
    
    bp->fun();
    bp->gun();
    bp->sun();
    bp->run();
    //bp->mun();  // error
    //bp->bun();  // error

    return 0;
}