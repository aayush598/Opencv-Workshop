import cv2 

webcam = cv2.VideoCapture(0)

while True:

    check, frame = webcam.read()
    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)

    if key == ord('s'): 
        cv2.imwrite(filename='saved_img.jpg', img=frame)
        webcam.release()
        cv2.destroyAllWindows()
        break

    elif key == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break