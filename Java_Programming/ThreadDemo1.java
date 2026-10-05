class ThreadDemo1{

    public static void main(String A[])
    {
        System.out.println("Inside main");

        Thread t = Thread.currentThread();

        System.out.println("Current thread name is : "+t.getName());    //main 

        System.out.println("Current thread TID is : "+t.getId());   //  3

        System.out.println("Thread is alive or not : "+ t.isAlive());   // true

        System.out.println("Thread priority is : "+t.getPriority());    // 5
    }
}