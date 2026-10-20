import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.*;

public class ChatClientDemo {
    public static void main(String A[]) throws Exception
    {
        Socket sobj = new Socket("localhost",5101);

        PrintStream pobj = new PrintStream(sobj.getOutputStream());
    
        BufferedReader bobj1 = new BufferedReader(new InputStreamReader(sobj.getInputStream()));

        BufferedReader bobj2 = new BufferedReader(new InputStreamReader((System.in)));

        pobj.println("Hi...");
        String str2;
        str2 = bobj1.readLine();

        System.out.println(str2);
    }
}
