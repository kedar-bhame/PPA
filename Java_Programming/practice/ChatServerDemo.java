import java.io.*;
import java.net.*;
import java.util.Scanner;

class ChatServerDemo {
    public static void main(String A[])throws Exception
    {
        // set up port 5101
        ServerSocket ssobj = new ServerSocket(5101);

        // accept socket connection
        Socket sobj = ssobj.accept();

        // printstream object to pass date to other 
        PrintStream pobj = new PrintStream(sobj.getOutputStream());

        // bufferedreader object to get data from other
        BufferedReader bobj1 = new BufferedReader(new InputStreamReader(sobj.getInputStream()));

        // class bufferedreader or scanner to accept user input from keyboard
        // BufferedReader bobj2 = new BufferedReader(new InputStreamReader(System.in));
        Scanner scanner = new Scanner(System.in);

        String str1;
        str1 = bobj1.readLine();
        System.out.println(str1);

        //
        pobj.println("Hello");
    }
    
}
