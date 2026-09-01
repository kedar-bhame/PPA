#include<iostream>
using namespace std;
class divA
{
    public:
        int i;
};
class divB
{
    public:
        int i;
};
class derived : public divA, public divB
{
    public:
        int k;
};
int main(){

    derived dobj;
    // dobj.i = 10;
    // dobj.j = 20;
    dobj.k = 30;
    cout<<sizeof(dobj)<<"\n";
    // cout<<dobj.i<<"\n";
    // cout<<dobj.j<<"\n";
    cout<<dobj.k<<"\n";

}