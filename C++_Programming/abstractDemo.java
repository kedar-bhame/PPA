abstract class Base
{
        public int i, j;

        public int Addition(int no1, int no2)  // 1000
        {
            return no1 + no2;
        }
        abstract int Substraction(int no1, int no2); //--------
}

class Derived extends Base
{
        public int x;
        public int Substraction(int no1, int no2)  // 2000
        {
            return no1 - no2;
        }
        public int Multiplication(int no1, int no2)    // 3000
        {
            return no1 * no2;
        }
}

class abstractDemo{
    public static void main(String A[])
    {
        Derived dobj = new Derived();
        int Ret = 0;
        
        Ret = dobj.Addition(11,10);
        System.out.println("Addition is : "+Ret);

        Ret = dobj.Substraction(11,10);
        System.out.println("Substraction is : "+Ret);

        Ret = dobj.Multiplication(11,10);
        System.out.println("Multiplication is : "+Ret);

        
    }
}