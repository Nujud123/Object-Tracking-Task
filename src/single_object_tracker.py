import cv2

# initialize CSRT tracker
tracker = cv2.TrackerKCF_create()

# start the live webcam stream
video = cv2.VideoCapture(0)

# read frames until 'q' pressed
while True:
    k, frame = video.read()
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(25) & 0xff == ord('q'):
        break

# ask user to select the ROI using bbox
bbox = cv2.selectROI(frame, False)

# track the selected object and close the window
ok = tracker.init(frame, bbox)
cv2.destroyWindow('ROI selector')

# keep track the object until 'q' pressed
while True:
    ok, frame = video.read()
    ok, bbox = tracker.update(frame)

    # update the bbox based on its coordinates
    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0]+bbox[2]),
              int(bbox[1]+bbox[3]))
        cv2.rectangle(frame, p1, p2, (0,0,255), 2, 2)

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
