import cv2

stream_url = "https://zssd-hippo.hls.camzonecdn.com/CamzoneStreams/zssd-hippo/chunklist.m3u8"  # <- wstaw tu pełny link

cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Nie udało się otworzyć strumienia")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Brak danych z kamery")
        break

    cv2.imshow("Hippo Cam", frame)

    # zapis pojedynczego frame'a
    cv2.imwrite("frame.jpg", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
