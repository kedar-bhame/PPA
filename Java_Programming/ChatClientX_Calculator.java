import java.io.*;
import java.net.*;


class ChatClientX {
    public static void main(String A[]) throws Exception
    {
        try
        {
        

            Socket sobj = new Socket("localhost",5100);
            System.out.println("Client get connected with server successfully.");

            PrintStream pobj = new PrintStream(sobj.getOutputStream());
            BufferedReader bobj1 = new BufferedReader(new InputStreamReader(sobj.getInputStream()));
            BufferedReader bobj2 = new BufferedReader(new InputStreamReader(System.in));

            System.out.println("Marvellous Client is running. ");
            String str1 = null, str2 = null;
            System.out.println("Enter message for server : ");
            str1 = bobj2.readLine();
            pobj.println(str1); // speaking
            
            
            
            
            
            str2 = bobj1.readLine();    // liseaning
            System.out.println("Server says : "+ str2);
            pobj.close();
            bobj1.close();
            bobj2.close();
            sobj.close();
            
        } // End of try
        catch(Exception eobj)
        {
            System.out.println(eobj);
        }
    } // End of main
} // End of class