import java.io.*;
import java.net.*;
import java.util.*;


class ChatClientX {
    public static void main(String A[]) throws Exception
    {
        try
        {
        

            Socket sobj = new Socket("localhost",5100);
            System.out.println("Client get connected with server successfully.");

            PrintStream pobj = new PrintStream(sobj.getOutputStream());
            BufferedReader bobj1 = new BufferedReader(new InputStreamReader(sobj.getInputStream()));
            // BuffredReader bobj2 = new BufferedReader(new InputStreamReader(System.in));
            Scanner scanner = new Scanner(System.in);

            System.out.println("Marvellous Client is running. ");
            int iNo1 = 0, iNo2 = 0;
            float output = 0.0f;
            String operation = null;
            System.out.println("Enter message for server first number : ");
            iNo1 = scanner.nextInt();
            pobj.println(iNo1); // speaking


            System.out.println("Enter message for server second number : ");
            iNo2 = scanner.nextInt();
            pobj.println(iNo2); // speaking
            
            
            System.out.println("Select operation like add, sub, mul, div ");
            operation = scanner.next();    
            pobj.println(operation);     // speaking 
            




            output = Float.parseFloat(bobj1.readLine());    // lisening
            System.out.println("Answer of "+iNo1+" "+operation+" "+iNo2+" is : "+output);
            pobj.close();
            bobj1.close();
            scanner.close();
            sobj.close();
            
        } // End of try
        catch(Exception eobj)
        {
            System.out.println(eobj);
        }
    } // End of main
} // End of class