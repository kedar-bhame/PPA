#include<iostream>
using namespace std;

class Demo
{
    public:
        int No1;
        int No2;
        static int X;

        Demo(int i, int j)
        {
            No1 = i;
            No2 = j;
            cout<<"Inside constructor\n";
        }

        void fun()
        {
            cout<<"Inside fun\n";
            cout<<No1<<"\n";
            cout<<No2<<"\n";
            cout<<X<<"\n";
        }

        static void gun()
        {
            cout<<"Inside gun\n";
            cout<<X<<"\n";
        }
};

int Demo :: X = 11; 

int main()
{
   cout<<Demo::X<<"\n";
   Demo::gun();

   Demo obj1(10,20);
   Demo obj2(30,40);

   obj1.fun();
   obj2.fun();
    
    return 0;
}