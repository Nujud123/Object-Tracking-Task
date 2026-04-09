from ultralytics import YOLO
import cv2

# load model
model = YOLO("assets/models/yolov8n.pt")

# load video
video_path = 'assets/videos/test1.mp4'
cap = cv2.VideoCapture(video_path)

selected_id = None

# read frames and select person
while True:
    success, frame = cap.read()

    if success:
        # detect and track person
        results = model.track(frame, persist=True, classes=[0], verbose=False)

        # plot results on the frame
        annotated_frame = results[0].plot()

        # display the frame
        cv2.imshow('Select Your Child ID', annotated_frame)

        # break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()

        selected_id = int(input('Enter your child ID: '))
        break
    else:
        break

# rewind the video to the first frame
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

while True:
    success, frame = cap.read()

    if success:
        # detect and track person
        results = model.track(frame, persist=True, classes=[0], verbose=False)

        # collect the boxes and the ids of the detected persons
        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.tolist()
            ids = [int(i) for i in results[0].boxes.id.tolist()]

            # search for selected person and store the new bbox coordinates
            for box, track_id in zip(boxes, ids):
                if track_id == selected_id:
                    x1, y1, x2, y2 = map(int, box)

                    # update the bbox based on its coordinates
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    cv2.putText(frame, f'Child ID: {track_id}', (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2,)
        
        # display the frame
        cv2.imshow('Singal Person Tracking', frame)

        # break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release the video and close windows    
cap.release()
cv2.destroyAllWindows()
