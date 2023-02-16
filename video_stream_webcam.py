import cv2

CamR = cv2.VideoCapture(1)
CamL = cv2.VideoCapture(0)


while True:
    retR, frameR= CamR.read()
    retL, frameL= CamL.read()

    cv2.imshow('imgR',frameR)
    cv2.imshow('imgL',frameL)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

CamR.release()
CamL.release()
cv2.destroyAllWindows()