import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Scanner;

public class IPAddressFinder {

    public static String getLocalIPAddress() {
        try {
            // Get the local host object
            InetAddress localHost = InetAddress.getLocalHost();
            
            // Get the local IP address
            return localHost.getHostAddress();
        } catch (UnknownHostException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static String getRemoteIPAddress(String remoteHost) {
        try {
            // Get the IP address of the remote host
            InetAddress remoteAddress = InetAddress.getByName(remoteHost);
            return remoteAddress.getHostAddress();
        } catch (UnknownHostException e) {
            return "Error: " + e.getMessage();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get and display local machine's IP address
        System.out.println("Local Machine IP Address: " + getLocalIPAddress());

        // Get and display IP address of a remote machine
        System.out.print("Enter the hostname or IP address of the remote machine: ");
        String remoteHost = scanner.nextLine();
        System.out.println("Remote Machine IP Address: " + getRemoteIPAddress(remoteHost));
        
        scanner.close();
    }
}
