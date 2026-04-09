# Object Tracking Task

For the task of creating a system that tracks a specific object in real time, I built two solutions using two different techniques. One uses a classic single-object tracker (KCF algorithm) and OpenCV, which is the solution that directly follows the task requirements, and the other was built for experimental purposes to track a single object using a multi-object tracker (YOLO model).

## Implementation Details
### Approach 1: Single Object Tracking using OpenCV
- The system captures a live video stream using the webcam.
- The user manually selects the target object using `cv2.selectROI()`.
- A KCF tracker is initialized using the selected bounding box.
- The tracker then follows the target frame by frame.

### Approach 2: YOLO-based tracking 
- The system processes a pre-recorded video as a simulated live stream.
- YOLO is used to detect people (a child in my use case) in each frame.
- A tracking ID is assigned to each detected person.
- The user selects the target ID, and the system tracks only that person throughout the video.

## Repository Structure
```
assets/
    models/                     # place the YOLO model weights here
    videos/                     # contains two videos to test the system
        test1.mp4               
        test2.mp4

src/
    single_object_tracker.py    # classical SOT 
    yolo_tracker.py             # MOT with target selection

.python-version
pyproject.toml
README.md
uv.lock
```

## How to Run Locally
### 1) Clone the repository
```bash
git clone https://github.com/Nujud123/Object-Tracking-Task.git
```
### 2) Create and sync the environment
This project uses [uv](https://docs.astral.sh/uv/) for dependency management.
```bash
uv sync
```
### 3) Run the SOT tracking implementation
```bash
uv run python src/single_object_tracker.py
```
### 4) Select an object to track
- After running the previous command, the camera will turn on.
- Press 'q' to pause the live stream.
- Draw a bounding box around the target object.
- Press 'Enter' or 'Space' to confirm the selection.
- The tracker will then follow the target.

### Optional: run the YOLO-based version
Important Note: If you want to try the YOLO-based version, use a different environment to avoid dependency conflicts with OpenCV tracker modules.
```bash
uv run python src/yolo_tracker.py
```

## Examples & Demo
### SOT Use case:
In this example, I targeted my plant by drawing a bounding box around it. This system can be used for more meaningful use cases and can be integrated with other systems like a bookshelf management system.

https://github.com/user-attachments/assets/24025536-a272-49cc-96fd-5856ca0e623f

### YOLO-based Use case:
I used this system to simulate monitoring children via a nursery camera. The parent enters their child's ID after the first frame is displayed. Then the tracker filters the IDs and displays a bounding box only around their child, making it easier for the parent to follow them.

https://github.com/user-attachments/assets/f582f5a7-eb44-48e8-9eb0-385f3127f96a

## Author
Nujud Almaleki

