import java.util.*;

class Selection3
{
    public static void main(String a[])
    {
        Scanner sobj = new Scanner(System.in);
        int No = 0;

        System.out.println("Enter your age : ");
        No = sobj.nextInt();

        if(No < 18){
            System.out.println("Not allowed ");
        }else{
            System.out.println("Allowed ");
        }
    }
}