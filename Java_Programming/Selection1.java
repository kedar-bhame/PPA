import java.util.*;

class Selection1
{
    public static void main(String a[])
    {
        Scanner sobj = new Scanner(System.in);
        int No = 0;

        System.out.println("Enter number: ");
        No = sobj.nextInt();

        if((No % 2) == 0){
            System.out.println("Even number ");
        }else{
            System.out.println("Odd number ");
        }
    }
}