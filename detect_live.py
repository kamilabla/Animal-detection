import cv2
import torch
# from yolov5.models.common import DetectMultiBackend
# from yolov5.utils.general import non_max_suppression, scale_coords
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'yolov5s') 

stream_url = "https://zssd-hippo.hls.camzonecdn.com/CamzoneStreams/zssd-hippo/chunklist.m3u8"  
cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Nie udało się otworzyć strumienia.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Brak klatki.")
        break

    results = model(frame) # process the frame with YOLOv5



    annotated_frame = results.render()[0]
    cv2.imshow('YOLO Hippo Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
