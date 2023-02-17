import numpy as np
import cv2


CamL= cv2.VideoCapture(0) # Left camera
CamR= cv2.VideoCapture(1) # Right camera

def main():

    image_id = 0

    while True:
        if not (CamL.grab() and CamR.grab()):
            print("No more frames")
            break

        _, left_frame = CamL.retrieve()
        _, right_frame = CamR.retrieve()

        cv2.imshow('capL', left_frame)
        cv2.imshow('capR', right_frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('c'):
            cv2.imwrite("office_images/left" + str(image_id) + ".png", left_frame)
            cv2.imwrite("office_images/right" + str(image_id) + ".png", right_frame)
            image_id += 1

    CamL.release()
    CamR.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
