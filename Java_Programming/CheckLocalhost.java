import java.net.InetAddress;

public class CheckLocalhost {
    public static void main(String[] args) {
        try {
            InetAddress[] addresses = InetAddress.getAllByName("localhost");
            for (InetAddress address : addresses) {
                System.out.println("Resolved Localhost: " + address.getHostAddress());
                if (address.getHostAddress().contains(":")) {
                    System.out.println("This is IPv6");
                } else {
                    System.out.println("This is IPv4");
                }
                
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
} 
// output - 
// Resolved Localhost: 127.0.0.1
// This is IPv4
// Resolved Localhost: 0:0:0:0:0:0:0:1
// This is IPv6
