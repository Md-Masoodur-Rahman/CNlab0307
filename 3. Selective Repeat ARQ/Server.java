import java.net.*;
import java.io.*;

public class Server {

    private static final int PORT = 12346; // Change the port number
    private static final String SHUTDOWN_MESSAGE = "shutdown"; // Shutdown message

    public static void main(String[] args) {
        try {
            DatagramSocket serverSocket = new DatagramSocket(PORT);
            System.out.println("Server started...");

            while (true) {
                byte[] receiveData = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                serverSocket.receive(receivePacket);
                String sentence = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("Received: " + sentence);

                // Check for shutdown message
                if (sentence.equals(SHUTDOWN_MESSAGE)) {
                    System.out.println("Shutdown command received. Server is shutting down.");
                    break;
                }

                // Simulate processing delay
                Thread.sleep(1000);

                // Send acknowledgment
                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();
                byte[] sendData = "ACK".getBytes();
                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, clientAddress, clientPort);
                serverSocket.send(sendPacket);
            }

            // Close the server socket
            serverSocket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
