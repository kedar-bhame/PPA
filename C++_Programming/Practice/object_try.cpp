// Source - https://stackoverflow.com/q/17716293
// Posted by lukai, modified by community. See post 'Timeline' for change history
// Retrieved 2026-09-23, License - CC BY-SA 4.0

#include <iostream>
using namespace std;

 class myclass{
    public:
        int a,b;
    public:
        void setdata(int i,int j){
            a=i;
            b=j;
        }
};

int main() {
    myclass *p;
    p = new myclass;
    cout<<p->a<<"\n";
    cout<<p->b<<"\n";
    p->setdata(5,6);
    cout<<p->a<<"\n";
    cout<<p->b<<"\n";
    return 0;
}
