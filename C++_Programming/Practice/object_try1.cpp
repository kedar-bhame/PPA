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
    p = new myclass[10];
    cout<<sizeof(*p)<<"\n";
    cout<<p->a<<"\n";
    cout<<p->b<<"\n";
    p[2].setdata(5,6);
    cout<<p[2].a<<"\n";
    cout<<p[2].b<<"\n";
    return 0;
}
