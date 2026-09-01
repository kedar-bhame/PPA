class Arithematic
{
    public int No1;
    public int No2;
    
    public Arithematic()
    {
        this.No1 = 0;
        this.No2 = 0;
    }
    public Arithematic(int i, int j)
    {
        this.No1 = i;
        this.No2 = j;
    }
    public int Addition()
    {
        int Ans = 0;
        Ans = this.No1 + this.No2;
        return Ans;
    }
    public int Substraction()
    {
        int Ans = 0;
        Ans = this.No1 - this.No2;
        return Ans;
    }
}

class OOPXX
{
    public static void main(String A[])
    {
        Arithematic aobj1 = new Arithematic(21,10);
        int Result = 0;
        Result = aobj1.Addition();

        System.out.println("Addition is : "+Result);

        Result = aobj1.Substraction();

        System.out.println("Substraction is : "+Result);
    }
}