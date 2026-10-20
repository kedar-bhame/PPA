import java.net.InetAddress;

public class LocalhostDemo
{
    public static void main(String A[]) throws Exception 
    {
        InetAddress localhost = InetAddress.getLocalHost();
        System.out.println("Localhost Name : "+localhost.getHostName());
        System.out.println("Localhost IP : "+localhost.getHostAddress());
        // Localhost Name : DESKTOP-85MN0RQ
        // Localhost IP : 192.168.1.33
    }
}