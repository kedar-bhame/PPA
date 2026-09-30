interface A
{
    void fun();
}

class B implements A
{
    public void fun()
    {
        System.out.println("Inside fun ");
    }
}

class InterfaceDemo{
    public static void main(String A[])
    {
        B bobj = new B();
        bobj.fun();
    }

}