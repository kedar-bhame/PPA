class Demo implements Runnable
{
    public void run()
    {
        System.out.println("Thread is running...");
    }
}

class ThreadDemo3{

    public static void main(String A[])
    {
        System.out.println("Inside main");

        Demo dobj1 = new Demo();
        Demo dobj2 = new Demo();

        dobj1.start();  // Error because implements does not have start method
        dobj2.start();  // Error

        
    }
}