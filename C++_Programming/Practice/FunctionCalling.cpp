#include<iostream>
using namespace std;

class Demo{
    public :
        int x, y ;
        Demo(){
            cout<<"inside Default Constructor. \n";
            this-> x = 0;
            this-> y = 0;
        }
        Demo(int a, int b)
        {
            cout<<"Inside Parameterised Constructor. \n";
            this-> x = a;
            this-> y = b;
        }
        Demo(Demo &ref){
            cout<<"Inside copy Constructor. \n";
            this-> x = ref.x;
            this-> y = ref.y;
        }
};

int main()
{
    class Demo dobj;
    cout<<"x = "<<dobj.x<<"\n";
    cout<<"y = "<<dobj.y<<"\n";

    class Demo dobj2(11,21);
    cout<<"x = "<<dobj2.x<<"\n";
    cout<<"y = "<<dobj2.y<<"\n";

    class Demo dobj3(dobj2);
    cout<<"x = "<<dobj3.x<<"\n";
    cout<<"y = "<<dobj3.y<<"\n";
    
    return 0;

}