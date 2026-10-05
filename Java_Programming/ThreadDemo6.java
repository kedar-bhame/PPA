class Demo extends Thread
{
    public void run()
    {
        System.out.println("Thread is running...");
    }
}

class ThreadDemo6{

    public static void main(String A[]) throws Exception
    {
        System.out.println("Inside main");

        Demo dobj1 = new Demo();
        Demo dobj2 = new Demo();

        dobj1.start();
        dobj2.start();

        dobj1.join();
        dobj2.join();

        System.out.println("End of main thread");   // Issue main thread is ending early without their child kalji

        
    }
}