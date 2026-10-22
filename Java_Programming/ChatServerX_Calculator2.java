import java.io.*;
import java.net.*;
import java.util.*;


class ChatServerX {
   public static void main(String A[])
    {
        try
        {
            ServerSocket ssobj = new ServerSocket(5100);
            System.out.println("Server is running at port 5100 ");
            Socket sobj = ssobj.accept();
            System.out.println("Client request get accepted successfully. ");

            PrintStream pobj = new PrintStream(sobj.getOutputStream());
            BufferedReader bobj1 = new BufferedReader(new InputStreamReader(sobj.getInputStream()));
            // BufferedReader bobj2 = new BufferedReader(new InputStreamReader(System.in));
            Scanner scanner = new Scanner(System.in);

            System.out.println("Marvellous Server is running. ");
            int iNo1 = 0, iNo2 = 0;
            float output = 0.0f;
            String operation = null;



            iNo1 = Integer.parseInt(bobj1.readLine());    // lisening 
            System.out.println("Client says first input : "+iNo1);



            iNo2 = Integer.parseInt(bobj1.readLine());    // lisening 
            System.out.println("Client says second input : "+iNo2);



            operation = bobj1.readLine();   // lisening
            System.out.println("Client says operation : "+operation);
            output = calculator(iNo1, iNo2, operation);
            pobj.println(output);   // speaking
            System.out.println("Final output send to client : "+output);


            pobj.close();
            bobj1.close();
            scanner.close();
            sobj.close();
            ssobj.close();
        } // End of try
        catch(Exception eobj)
        {
            System.out.println(eobj);
        }
    } // End of main

    ////////////////////////////////////////////////////////////////////////
    //
    // Function Name    :   calculator
    // Description      :   perform basic add,sub,mul,div calculation
    // Input            :   Interger, Interger, String
    // Output           :   Interger   
    // Author           :   Kedar Anant Bhame
    // Date             :   22/10/2026
    //
    /////////////////////////////////////////////////////////////////////////


    static int calculator(int iValue1, int iValue2, String operation)
    {
        switch(operation)
        {
            case "add":
                return (iValue1 + iValue2);
            case "sub":
                return (iValue1 - iValue2);
            case "mul":
                return (iValue1 * iValue2);
            case "div":
                return (iValue1 / iValue2);
            default:
                return -1;
        } // End of switch
    } // End of calculator
} // End of class