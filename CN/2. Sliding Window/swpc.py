def main():
    # Prompt the user to enter the window size
    window_size = int(input("Enter window size: "))
    
    # Prompt the user to enter the number of frames to transmit
    num_frames = int(input("Enter number of frames to transmit: "))
    
    # Allow the user to enter the frames
    frames = []
    print(f"Enter {num_frames} frames: ")
    for i in range(num_frames):
        frames.append(input())
    
    print("\nWith sliding window protocol, the frames will be sent in the following way (assuming no corruption of frames):")
    
    # Simulate sending frames in windows
    i = 0
    while i < num_frames:
        print(f"\nSending frames: {frames[i:i+window_size]}")
        input("\nPress Enter to send acknowledgment...")
        print("Acknowledgement of above frames sent is received by sender")
        
        i += window_size

if __name__ == "__main__":
    main()
