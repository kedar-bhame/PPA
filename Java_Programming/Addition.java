import java.util.Scanner;
class Addition
{
    public static void main(String A[])
    {
        int No1 = 0, No2 = 0, Ans = 0;
        Scanner sobj = new Scanner(System.in);
        System.out.println("Enter first number : ");
        No1 = sobj.nextInt();

        System.out.println("Enter second number : ");
        No2 = sobj.nextInt();

        Ans = No1 + No2;

        System.out.println("Addition is : "+Ans);
        
    }
}