-
- Works with webcam input or pre-recMoving Object Detection using OpenCV
  ## 📌 Overview
  This project implements Moving Object Detection using OpenCV in Python. The program detects motion in a video feed by processing frames and highlighting moving objects.
  ## 🛠️ Technologies Used
  - Python
  - OpenCV
  - NumPy
  ## 🚀 Features
  - Detects motion in real-time from a video stream.
  - Highlights moving objects.orded video.

## 📂 Project Structure

```
├── main.py  # Main script for motion detection
├── video.mp4  # (Optional) Sample video for testing
├── requirements.txt  # List of dependencies
├── README.md  # Project documentation
```

## 🔧 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/moving-object-detection.git
   cd moving-object-detection
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the project:
   ```sh
   python main.py
   ```

## 📜 How It Works

1. The program reads frames from a video or webcam.
2. It converts frames to grayscale and applies Gaussian blur.
3. A background subtraction method detects moving objects.
4. Bounding boxes highlight detected motion.


