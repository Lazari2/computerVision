import cv2
import mediapipe
import pyautogui

face_mesh_landmarks = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
camera = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()
while True:
    _,img = camera.read()
    img = cv2.flip(img,1)
    window_h, window_w, _ = img.shape
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    processed_img = face_mesh_landmarks.process(rgb_image)
    all_face_landmarks_points = processed_img.multi_face_landmarks

    if all_face_landmarks_points:
        one_face_landmark_points = all_face_landmarks_points[0].landmark
        for id, landmark_point in enumerate(one_face_landmark_points[474:478]):
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
           #print(x,y)
            if id==1:
                mouse_x = int(screen_w / window_w * x)
                mouse_y = int(screen_h /window_h * y)
                pyautogui.moveTo(mouse_x,mouse_y)

            cv2.circle(img,(x,y),3,(0,0,255))

        left_eye = [one_face_landmark_points[145], one_face_landmark_points[159]]
        for landmark_point in left_eye:
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
           # print(x,y)
            cv2.circle(img,(x,y),3,(0,255,255))
        
        if(left_eye[0].y - left_eye[1].y<0.01):
            pyautogui.click()
            pyautogui.sleep(1)
            print('click')

    cv2.imshow("Eye mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows() 