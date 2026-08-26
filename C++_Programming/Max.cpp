#include<iostream>
using namespace std;

class Operation
{
    public:
        int Addition(int a, int b)
        {
            int Result = 0;
            Result = a + b;
            return Result ;
        }
};
int main()
{
    int x = 10, y = 12, Ans = 0;
    Operation oobj;
    
    Ans = oobj.Addition(x,y);
    
    cout<<Ans<<"\n";

    return 0;
}