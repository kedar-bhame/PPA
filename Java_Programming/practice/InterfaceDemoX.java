
interface A
{   
    int i = 11;
    void fun();
}

class B implements A
{
    public void fun()
    {
        System.out.println("Inside fun ");
    }
}

class InterfaceDemoX{
    public static void main(String A[])
    {
        System.out.println(B.i);
        // B.i++;  // Error 
    }

}