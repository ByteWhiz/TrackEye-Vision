# TrackEye Vision: Motion Detection with OpenCV

![TrackEye Vision Animation](path_to_animation.gif) <!-- Replace with the path to your animation GIF -->

## Project Overview

**TrackEye Vision** is a Python-based motion detection system leveraging OpenCV, designed to enhance security and monitoring capabilities. The application captures video from a webcam, detects motion, and records video clips only when movement is detected. The system is optimized for various surveillance scenarios, including home security and vehicle monitoring. Future enhancements will include sending SMS alerts for suspicious movements and integrating a database to track numbers detected near specific areas. Powered by solar energy, TrackEye Vision is an eco-friendly solution ideal for remote or off-grid deployment.

## Features

- **Real-Time Video Capture**: Utilizes the default webcam to provide continuous live video monitoring.
- **Motion Detection**: Detects movement using frame differencing and contour detection, ensuring recordings are only made when motion is present.
- **Timestamp Overlay**: Each frame includes a timestamp, helping to accurately log the time of each event.
- **Automated Directory Management**: Automatically creates and manages an output folder on the desktop to store recorded videos.
- **Eco-Friendly Operation**: Designed to run on solar power, significantly reducing energy consumption and enabling remote usage.

## Future Enhancements

- **SMS Alerts**: The system will send real-time SMS notifications for detected suspicious movements, ensuring immediate awareness and response.
- **Database Integration**: Implementation of a database to log and track numbers detected near monitored areas, providing comprehensive monitoring capabilities.
- **Weekly Server Cleanup**: Recorded videos will be uploaded to a server, and the local storage will be cleaned weekly to optimize storage and maintain efficiency.

## How It Works

1. **Video Capture Initialization**: TrackEye Vision starts by accessing the webcam using OpenCV's `VideoCapture`.
2. **Motion Detection**: Compares current frames with a reference frame to detect significant changes that indicate motion.
3. **Contour Detection**: Applies thresholding and finds contours to accurately identify and outline areas of detected motion.
4. **Recording Trigger**: Automatically begins recording and saving video when motion is detected, ensuring only relevant footage is captured.
5. **Display and Interaction**: Provides a live video feed with motion-marked areas and timestamps. Users can exit the application by pressing 'q'.

## How to Run the Project

1. **Install Required Libraries**: Ensure Python and necessary libraries are installed:
    ```bash
    pip install opencv-python
    ```
2. **Run the Script**: Execute the script to start monitoring:
    ```bash
    python trackeye_vision.py
    ```
3. **Exit the Application**: Press 'q' to stop monitoring and exit the application.

## Output

- Videos are stored in the `records` folder on the desktop, named using the current date and time to ensure unique file names.

## Potential Use Cases

- **Vehicle Security**: Monitor and track activities around a vehicle, sending alerts and logging events for unauthorized access or movement.
- **Home Surveillance**: Secure homes with real-time monitoring, providing alerts and recording evidence for security breaches.
- **Wildlife Monitoring**: Deploy in remote areas using solar power for continuous wildlife observation, ensuring minimal human interference.

## Project Dependencies

- Python 3.x
- OpenCV (`opencv-python`)

---


