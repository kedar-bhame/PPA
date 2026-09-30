import java.util.*;

class ExceptionDemo2
{
    public static void main(String[] args) {
        {
            Scanner sobj = new Scanner(System.in);

            int Arr[] = {11,21,51,101,111};
            int index = 0;

            System.out.println("Enter the index");
            index = sobj.nextInt();


            System.out.println("Element is : "+Arr[index]);

            System.out.println("End of main");
        }
    }
}