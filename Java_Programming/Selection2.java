import java.util.*;

class Selection2
{
    public static void main(String a[])
    {
        Scanner sobj = new Scanner(System.in);
        int No = 0;

        System.out.println("Enter your age : ");
        No = sobj.nextInt();

        if(No >= 18){
            System.out.println("Allowed ");
        }else{
            System.out.println("Not allowed ");
        }
    }
}