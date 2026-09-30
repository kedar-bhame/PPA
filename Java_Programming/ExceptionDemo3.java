import java.util.*;

class Demo{
    public static int Division(int No1, int No2){
        return No1 / No2;
    }
}

class ExceptionDemo3
{
    public static void main(String[] args) {
        {
            Scanner sobj = new Scanner(System.in);

            int No1 = 0, No2 = 0, Ans = 0;

            System.out.println("Enter first number");
            No1 = sobj.nextInt();

            System.out.println("Enter second number");
            No2 = sobj.nextInt();

            Ans = Demo.Division(No1, No2);    // Exception prone code

            System.out.println("Division is : "+Ans);
        }
    }
}