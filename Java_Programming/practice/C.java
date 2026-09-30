interface A
{   
    int i = 11;
    void fun();
}
interface B
{
    void fun();
}
public class C implements A,B
{
    public void fun()
    {
        System.out.println("Inside fun of class C ");
    }
}

class InterfaceDemoXX{
    public static void main(String A[])
    {
        System.out.println(C.i);
        // B.C++;  // Error 
        C.fun();
    }

}