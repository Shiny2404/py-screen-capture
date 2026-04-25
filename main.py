import cv2
import numpy as np
import pyautogui

# Get screen size
screen_size = pyautogui.size()

# Define video codec and output file
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("screen_record.avi", fourcc, 20.0, screen_size)

print("Recording started... Press 'q' to stop")

while True:
    # Take screenshot
    img = pyautogui.screenshot()
    
    # Convert screenshot to numpy array
    frame = np.array(img)
    
    # Convert RGB to BGR (OpenCV format)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Write frame to video file
    out.write(frame)
    
    # Show recording screen (optional)
    cv2.imshow("Screen Recorder", frame)

    # Stop recording when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
out.release()
cv2.destroyAllWindows()