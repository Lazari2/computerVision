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
        for landmark_point in one_face_landmark_points:
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
           #print(x,y)
    
            cv2.circle(img,(x,y),3,(0,0,255))

    cv2.imshow("Landmarks", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()