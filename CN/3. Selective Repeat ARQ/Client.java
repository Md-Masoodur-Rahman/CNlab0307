import java.net.*;
import java.io.*;

public class Client {

    private static final String SERVER_IP = "localhost";
    private static final int SERVER_PORT = 12346; // Change the port number
    private static final String SHUTDOWN_MESSAGE = "shutdown"; // Shutdown message

    public static void main(String[] args) {
        try {
            DatagramSocket clientSocket = new DatagramSocket();
            InetAddress serverAddress = InetAddress.getByName(SERVER_IP);
            BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));

            while (true) {
                System.out.print("Enter message to send (type 'shutdown' to stop the server): ");
                String sentence = inFromUser.readLine();
                byte[] sendData = sentence.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, serverAddress, SERVER_PORT);
                clientSocket.send(sendPacket);

                // Check for shutdown message
                if (sentence.equals(SHUTDOWN_MESSAGE)) {
                    System.out.println("Shutdown command sent. Waiting for server response...");
                    break;
                }

                // Receive acknowledgment
                byte[] receiveData = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                clientSocket.receive(receivePacket);
                String ackMessage = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("ACK received: " + ackMessage);
            }

            // Close the client socket
            clientSocket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
