import java.util.Scanner;

public class IPAddressInfo {

    public static String getIpClass(String ipAddress) {
        int firstOctet = Integer.parseInt(ipAddress.split("\\.")[0]);
        if (firstOctet <= 127) {
            return "A";
        } else if (firstOctet <= 191) {
            return "B";
        } else if (firstOctet <= 223) {
            return "C";
        } else if (firstOctet <= 239) {
            return "D (Multicast)";
        } else {
            return "E (Reserved)";
        }
    }

    public static String getSubnet(String ipAddress) {
        String ipClass = getIpClass(ipAddress);
        switch (ipClass) {
            case "A":
                return "255.0.0.0";
            case "B":
                return "255.255.0.0";
            case "C":
                return "255.255.255.0";
            default:
                return "N/A (Class " + ipClass + " has no subnet)";
        }
    }

    public static String getNetworkId(String ipAddress) {
        String ipClass = getIpClass(ipAddress);
        String[] octets = ipAddress.split("\\.");
        switch (ipClass) {
            case "A":
                return octets[0];
            case "B":
                return octets[0] + "." + octets[1];
            case "C":
                return octets[0] + "." + octets[1] + "." + octets[2];
            default:
                return "N/A (Class " + ipClass + " has no network ID)";
        }
    }

    public static String getHostId(String ipAddress) {
        String ipClass = getIpClass(ipAddress);
        String[] octets = ipAddress.split("\\.");
        switch (ipClass) {
            case "A":
                return octets[1] + "." + octets[2] + "." + octets[3];
            case "B":
                return octets[2] + "." + octets[3];
            case "C":
                return octets[3];
            default:
                return "N/A (Class " + ipClass + " has no host ID)";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an IP address: ");
        String ipAddress = scanner.nextLine();

        String ipClass = getIpClass(ipAddress);
        String subnet = getSubnet(ipAddress);
        String networkId = getNetworkId(ipAddress);
        String hostId = getHostId(ipAddress);

        System.out.println("IP Class: " + ipClass);
        System.out.println("Subnet: " + subnet);
        System.out.println("Network ID: " + networkId);
        System.out.println("Host ID: " + hostId);

        scanner.close();
    }
}
