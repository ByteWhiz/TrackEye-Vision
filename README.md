# TrackEye Vision

## Project Overview

**TrackEye Vision** is an advanced motion detection and surveillance system utilizing Python and OpenCV. The system captures live video feed from a webcam, detects motion, and records video clips only when movement is detected. Designed for versatile security applications, TrackEye Vision is set to provide real-time monitoring, alerting, and recording capabilities, making it an ideal solution for both personal and professional use. Future enhancements include SMS alert notifications and a database for logging numbers detected near specific areas, such as vehicles. The system is powered by solar energy, ensuring sustainability and remote operation.

## Features

- **Real-Time Video Monitoring**: Uses a webcam to provide continuous video feed for live monitoring.
- **Intelligent Motion Detection**: Detects motion through frame differencing, recording only when movement is present.
- **Timestamp Overlay**: Each frame includes a timestamp for accurate event logging.
- **Efficient Recording**: Records and stores video clips in a designated folder, conserving space by recording only when necessary.
- **Eco-Friendly**: Designed to operate using solar power, reducing the environmental footprint and enabling off-grid deployment.
- **Weekly Cleanup**: Automatically cleans up older recordings every week to maintain server storage efficiency.

## Future Enhancements

- **SMS Alerts**: Implementing SMS notifications to alert users of suspicious movements in real-time.
- **Database Logging**: Adding a database to log detected numbers, providing detailed monitoring and security tracking.
- **Server-Based Storage**: Transition to server storage for scalability and remote access to recordings.

## How It Works

1. **Video Capture Initialization**: TrackEye Vision begins by initializing the webcam using OpenCV's `VideoCapture`.
2. **Motion Detection**: Compares each frame to a reference frame to detect significant changes indicative of motion.
3. **Recording Activation**: Starts recording video when motion is detected, marking the areas of movement.
4. **Live Feed Display**: Displays a live feed with marked motion areas and timestamps. Users can exit the feed by pressing 'q'.

## How to Run TrackEye Vision

1. **Install Required Libraries**: Ensure you have Python installed, then install OpenCV using pip:
    ```bash
    pip install opencv-python
    ```
2. **Run the Script**: Execute the following command to start the application:
    ```bash
    python trackeye_vision.py
    ```
3. **Stop the Application**: Press 'q' to exit the monitoring application.

## Output

- Recorded video clips are saved in a `records` folder on the desktop, named using the date and time format to ensure unique file names and prevent overwriting.

## Project Dependencies

- Python 3.x
- OpenCV (`opencv-python`)

## Use Cases

- **Vehicle Surveillance**: Monitor and record activities around a vehicle, with future capabilities for sending real-time alerts.
- **Home Security**: Provide real-time surveillance for home security, with recorded evidence stored securely.
- **Wildlife Observation**: Use solar-powered operation for remote monitoring of wildlife, ensuring sustainable and non-intrusive observation.

## How to Upload the Project to GitHub

1. **Create a GitHub Repository**: Log in to GitHub and create a new repository named "TrackEye Vision".
2. **Initialize a Local Git Repository**: Navigate to your project directory and initialize a git repository:
    ```bash
    git init
    ```
3. **Add Project Files**: Add all the files of your project to the repository:
    ```bash
    git add .
    ```
4. **Commit Changes**: Commit the added files with a message:
    ```bash
    git commit -m "Initial commit for TrackEye Vision project"
    ```
5. **Link to GitHub**: Set up the remote repository link:
    ```bash
    git remote add origin https://github.com/yourusername/TrackEye-Vision.git
    ```
6. **Push to GitHub**: Upload your project to GitHub:
    ```bash
    git push -u origin main
    ```

Replace `yourusername` with your GitHub username, and follow any prompts to authenticate and complete the process. Your project will now be available on GitHub, allowing others to access, clone, and contribute to it.

---

This README file, saved as `README.md`, is ready to be included in your project directory. Let me know if you need further assistance or more information!
