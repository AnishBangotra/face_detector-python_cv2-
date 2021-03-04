import cv2, time
def image_face_detector():
    new_path = "C:\\users\\Anish\\Appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\cv2"
#load cascade classifier training file for haarcascade
    face_cascade = cv2.CascadeClassifier(new_path + '\\data\\haarcascade_frontalface_default.xml')
    img=cv2.imread("D:\\PHOTOS\\IMG_0286.JPG",1)
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#This converting colour image in grey image there
    faces=face_cascade.detectMultiScale(grey_img, 1.1,5)#Scale factor here decrease the shape value by 5% until the face is found , smaller the scale factor value, greater is the accuracy.
    for x,y,w,h in faces:
        img=cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
    resized_img=cv2.resize(img, (int(img.shape[1]/5), int(img.shape[0]/5)))
    cv2.imshow('friends',resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_face_detector()

def cam_screen_shot():
    video=cv2.VideoCapture(0)
    check,frame=video.read()
    print(frame)
    cv2.imshow('screen_shot',frame)
    cv2.waitKey(0)
    video.release()
    cv2.destroyAllWindows()

def cam_Recorder():
    video=cv2.VideoCapture(0)
    count_frames=0
    while True:
        count_frames+=1
        check,frame=video.read()
        print(frame)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('capture', gray)
        key=cv2.waitKey(1)
        if key==ord('s'):
            break
    print(count_frames)
    video.release()
    cv2.destroyAllWindows()


def cam_face_detector():
    new_path = "C:\\users\\Anish\\Appdata\\local\\programs\\python\\python38-32\\lib\\site-packages\\cv2"
    face_cascade=cv2.CascadeClassifier(new_path + '\\data\\haarcascade_frontalface_default.xml')
    video=cv2.VideoCapture(0)
    count_frames=0
    while True:
        count_frames+=1
        check,frame=video.read()
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray, 1.1, 4)
        for x,y,w,h in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.imshow('img', frame)
        key=cv2.waitKey(1)
        if key==ord('s'):
            break
    print(count_frames)
    video.release()
    cv2.destroyAllWindows()
