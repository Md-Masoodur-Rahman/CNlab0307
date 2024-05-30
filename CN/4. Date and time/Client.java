import java.io.*;
import java.net.*;

public class Client {

    private static final String SERVER_IP = "localhost";
    private static final int SERVER_PORT = 12345;

    public static void main(String[] args) {
        try {
            // Connect to the server
            Socket socket = new Socket(SERVER_IP, SERVER_PORT);
            System.out.println("Connected to server...");

            // Create input stream to receive response from server
            InputStream inputStream = socket.getInputStream();
            BufferedReader in = new BufferedReader(new InputStreamReader(inputStream));

            // Send request to server
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            out.println("Request for current date and time");

            // Receive response from server
            String response = in.readLine();
            System.out.println("Response from server: " + response);

            // Close resources
            in.close();
            out.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
