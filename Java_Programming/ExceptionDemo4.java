import java.util.*;

class AgeInvalid extends Exception
{
    public AgeInvalid(String str)
    {
        super(str);
    }
}

class ExceptionDemo4
{
    public static void main(String[] args) 
    {
        {
            Scanner sobj = new Scanner(System.in);
            int Age = 0;

            System.out.println("Enter your age :");
            Age = sobj.nextInt();

            try
            {
                if (Age < 18)
                {
                    throw new AgeInvalid("You are under age");
                }
                else
                {
                    System.out.println("Welcome to -------");
                }
            }
            catch(AgeInvalid aobj)
            {
                System.out.println("Exception occour due to  "+aobj);
            }   
        }
    }
}