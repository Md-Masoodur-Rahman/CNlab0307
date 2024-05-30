import java.util.Scanner;

public class SlidingWindowProtocol {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Prompt the user to enter the window size
        System.out.print("Enter window size: ");
        int windowSize = scanner.nextInt();
        
        // Prompt the user to enter the number of frames to transmit
        System.out.print("Enter number of frames to transmit: ");
        int numFrames = scanner.nextInt();
        
        // Allow the user to enter the frames
        int[] frames = new int[numFrames];
        System.out.println("Enter " + numFrames + " frames:");
        for (int i = 0; i < numFrames; i++) {
            frames[i] = scanner.nextInt();
        }
        
        System.out.println("\nWith sliding window protocol, the frames will be sent in the following way (assuming no corruption of frames):");
        
        // Simulate sending frames in windows
        int i = 0;
        while (i < numFrames) {
            System.out.println("\nSending frames: " + getFramesString(frames, i, windowSize));
            waitForAcknowledgment();
            System.out.println("Acknowledgement of above frames sent is received by sender");
            
            i += windowSize;
        }
        
        scanner.close();
    }
    
    // Helper method to format frames in a window
    private static String getFramesString(int[] frames, int start, int windowSize) {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = start; i < Math.min(start + windowSize, frames.length); i++) {
            sb.append(frames[i]);
            if (i < start + windowSize - 1 && i < frames.length - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }
    
    // Helper method to simulate waiting for acknowledgment
    private static void waitForAcknowledgment() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("\nPress Enter to send acknowledgment...");
        scanner.nextLine();
    }
}
