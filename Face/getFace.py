import cv2
import numpy as np
import os #디렉터리 생성을 위해서--> user 얼굴 캡쳐 후 넣는 파일 생성


face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_extractor(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return None

    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face


#사용자의 얼굴을 저장할 faces 폴더의 유무 확인-> 없다면 생성!
if not os.path.isdir('face/'):
    os.makedirs('face/')    
    
face_dirs = 'face/'

#여기 원래 웹에서 파라미터 전달하려 해쏘
name= '1971454'

if not os.path.isdir(face_dirs + name):
    os.makedirs(face_dirs + name)


cap = cv2.VideoCapture(0)
count = 0


while True:
    ret, frame = cap.read()
    cv2.imshow('Face Capture',frame)
#엔터 누르면 사진 찍힘! 본인이 얼굴 각도 돌려가면서 100장 찍으면 됨
#엔터 쭉 누르면 연속촬영
    if cv2.waitKey(1)==13:
        
        if face_extractor(frame) is not None:
            count+=1
            face = cv2.resize(face_extractor(frame),(200,200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    
            file_name_path = face_dirs + name + '/user'+str(count)+'.jpg'
            cv2.imwrite(file_name_path,face)
            cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow('Face Cropper',face)
        else:
            print("Face not Found")
            pass
#esc 누르면 종료
    if cv2.waitKey(1)==27 or count==100:
        break

cap.release()
cv2.destroyAllWindows()
print('Colleting Samples Complete!!!')

