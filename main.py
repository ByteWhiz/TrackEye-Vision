import cv2
import os
import datetime

# Set up video capture
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_folder = os.path.join(os.path.expanduser('~'), 'Desktop', 'records')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
output_file = os.path.join(output_folder, f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.mp4')
out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

# Set up motion detection parameters
motion_threshold = 5000
frame_delta_threshold = 25
first_frame = None

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame cannot be read, break the loop
    if not ret:
        break

    # Convert frame to grayscale and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # If this is the first frame, initialize it
    if first_frame is None:
        first_frame = gray
        continue

    # Compute the absolute difference between the current frame and the first frame
    frame_delta = cv2.absdiff(first_frame, gray)
    thresh = cv2.threshold(frame_delta, frame_delta_threshold, 255, cv2.THRESH_BINARY)[1]

    # Dilate the thresholded image to fill in holes
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    thresh = cv2.dilate(thresh, kernel, iterations=4)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours
    motion_detected = False
    for contour in contours:
        # Ignore small contours
        if cv2.contourArea(contour) < motion_threshold:
            continue

        # Motion detected
        motion_detected = True

        # Draw the bounding box of the contour on the frame
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Add date and time overlay
    date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cv2.putText(frame, date_time, (10, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    # If motion is detected, record the video
    if motion_detected:
        out.write(frame)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()