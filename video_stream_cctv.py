from multiprocessing import Process as p
from multiprocessing import Event as e
from time import sleep
import cv2

def show_cam(cam, window_name, flag):
    capture= cv2.VideoCapture(cam) 
    while not flag.is_set():
        ret, frame = capture.read()
        cv2.imshow(window_name, frame)
        cv2.waitKey(10)
        if 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
    print("Returned!")


if __name__ == "__main__":

    CamL = 'something something' #Adress for CCTV
    CamR = 'something something' #Adress for CCTV


    e1 = e()
    e2 = e()

    print("Starting processes...")

    p1 = p(target=show_cam, args=(CamR, "right", e1))
    p2 = p(target=show_cam, args=(CamL, "left", e2))

    p1.start()
    p2.start()

    # sleep(5)
    # e1.set()
    # print("Right cam stopped!")
    # sleep(5)
    # e2.set()
    # print("Left cam stopped!")

    p1.join()
    p2.join()
