import cv2

# Open the video files
video_files = [
    r'C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\NEW_AP\video\traffic_roaad.mp4',
    r'C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\NEW_AP\video\road_vid.mp4',
    r'C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\NEW_AP\video\twitter.mp4',
    r'C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\NEW_AP\video\traffic_roaad.mp4',
    r'C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\NEW_AP\video\road_vid.mp4',
    r'C:\Users\LENOVO\OneDrive\Desktop\DEVSOC\NEW_AP\video\twitter.mp4',
    # Add paths for other video files here
]

# Initialize video capture objects
caps = [cv2.VideoCapture(file) for file in video_files]

# Create a window to display the frames
cv2.namedWindow('Multi-Video', cv2.WINDOW_NORMAL)

# Set the number of rows and columns for the grid layout
rows = 2
cols = 3

# Loop through the video frames
while True:
    # Read frames from each video source
    frames = []
    for i in range(len(video_files)):
        ret, frame = caps[i].read()
        if not ret:
            # Break the loop if any of the video sources reaches the end
            break
        print("Camera ",i+1," : ",frame[0][0])
        frames.append(frame)

    # Break the loop if any of the video sources reaches the end
    if len(frames) != len(video_files):
        break

    # Resize each frame to fit in the grid
    resized_frames = [cv2.resize(frame, (int(frames[0].shape[1] / cols), int(frames[0].shape[0] / rows))) for frame in frames]

    # Concatenate the resized frames horizontally
    row_frames = [cv2.hconcat(resized_frames[i * cols:(i + 1) * cols]) for i in range(rows)]

    # Concatenate the row frames vertically to create the grid
    grid_frame = cv2.vconcat(row_frames)

    # Display the grid frame
    cv2.imshow('Multi-Video', grid_frame)

    delay = 25  # You can adjust this value to slow down or speed up the video playback

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# Release the video capture objects and close OpenCV windows
for cap in caps:
    cap.release()
cv2.destroyAllWindows()
