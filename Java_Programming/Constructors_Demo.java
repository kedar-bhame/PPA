class Demo
{
    public Demo()
    {
        System.out.println("Inside Default constuctor");
    }

    public Demo(int i, int j)
    {
        System.out.println("Inside Parametrised constuctor");
    }
}

class Constructors_Demo
{
    public static void main(String A[])
    {
        Demo dobj1 = new Demo();
        Demo dobj2 = new Demo(11,21);
    }
}