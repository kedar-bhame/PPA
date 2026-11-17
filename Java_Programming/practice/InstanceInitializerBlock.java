class InstanceInitializerBlock
{
    {
        System.out.println("Inside initializer block");
    }

    static
    {
        System.out.println("Inside Static initializer block");
    }

    public InstanceInitializerBlock()
    {
        System.out.println("Object Created");
    } 

    public static void main(String A[])
    {
        InstanceInitializerBlock iobj1 = new InstanceInitializerBlock();
        InstanceInitializerBlock iobj2 = new InstanceInitializerBlock();

    }
}