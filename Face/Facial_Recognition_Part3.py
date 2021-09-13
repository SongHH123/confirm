import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import time # time.sleep 함수 때문에 모듈 불러옴
import threading
#LBP 알고리즘을 통해 모델 생성-> 얼굴 학습

name= '1971454'
#data_path = 'faces/' + name + '/'
data_path = 'faces/'

stu_faces = [f for f in listdir(data_path) if isfile(join(data_path,f))]

#데이터와 매칭될 라벨 변수
Training_Data, Labels = [], []

for i, files in enumerate(stu_faces):
    image_path = data_path + stu_faces[i]
#이미지를 흑백으로 읽어옴
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#TRAINING 데이터 리스트에 이미지를 바이트배열로 추가
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)
# 라벨을 정수로
Labels = np.asarray(Labels, dtype=np.int32)
#모델 생성 <- lbph를 사용할 새 변수 생성
model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Training_Data), np.asarray(Labels))

print("Model Training Complete!!!!!")

#얼굴형 인식
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


#LBP 방식으로 눈코입- 얼굴 인식
def face_detector(img, size = 0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #scaleFactor=1.3 (1.3배), minNeigh bors=5 (사각형이 유지해야하는 이웃 수,
    #                                       클수록 감지 적고, 품질 높고)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
#사진에 얼굴이 없다면
    if faces is():
        return img,[]

    for(x,y,w,h) in faces: #직사각형 크기로 얼굴 반환-> CROP
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200,200))

    return img,roi

#------------------------------------------------------------------------------------
# 10분에 한번 학생의 카메라로 학생 사진을 가져온다.
# 서버에서 출석 인정시간 가져오기 MAX_count= nn분--> / 10 --> 10분 나눈걸 max
# MAX_Check= Checktime / 10, 최대 출석 횟수= 출석인정시각(분) / 10
# 10분에 한번 방식 말고--> 최대 확인 횟수 정해서 , 전체시간 / 확인 횟수--> 6분이나 7분정도도 나올듯
Checktime= 70
MAX_Check= int (Checktime / 10)
attend_cnt= 0
CheckCount = 0

def Checking_Attend():
    global attend_cnt
    global CheckCount
    ck=0
    cap = cv2.VideoCapture(0)
    
    while True:
        
        ret, frame = cap.read()
        image, face = face_detector(frame)
    
        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            result = model.predict(face)
    
            if result[1] < 500:
 
                confidence = int(100*(1-(result[1])/300))    
    
            if confidence > 75:
                attend_cnt += 1
                CheckCount += 1
                print('attend')
                print(attend_cnt)
                print(CheckCount)
                cap.release()
                break
            else:
                print('run')
                ck+= 1
# 얼굴 구도로 인한 인식 오류 가능성-> 50초 동안 재검사 진행
                time.sleep(5)
                pass

            if ck >= 10:
                CheckCount += 1
                break

#얼굴 못찾으면 찾을 때 까지 진행
        except:
            pass
 
for _ in range( 0, MAX_Check):
    Checking_Attend()
    time.sleep(600) #10분에 한번 진행

# 만약 2번 이상 차이가 난다면.
if ( CheckCount > attend_cnt + 1) :
    # 결석 결과를 학생 출석 확인 및 선생 페이지에 전달
    print('결석')
else:
    print('출석') #정상출석!
