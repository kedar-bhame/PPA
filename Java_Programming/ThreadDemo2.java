class Demo extends Thread
{
    public void run()
    {
        System.out.println("Thread is running...");
    }
}

class ThreadDemo2{

    public static void main(String A[])
    {
        System.out.println("Inside main");

        Demo dobj1 = new Demo();
        Demo dobj2 = new Demo();

        dobj1.start();
        dobj2.start();

        
    }
}