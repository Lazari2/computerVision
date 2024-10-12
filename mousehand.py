import cv2
import mediapipe
import pyautogui

cam = cv2.VideoCapture(0)
capture_hands = mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
screen_widht, screen_height = pyautogui.size()
x1 = y1 = x2 = y2 = 0

while True:

    _,img = cam.read()
    img_height, img_widht, _ =img.shape
    img = cv2.flip(img, 1)
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output_hands = capture_hands.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(img, hand)
            one_hand_landmarks = hand.landmark
            for id, lm in enumerate(one_hand_landmarks):
                x = int(lm.x * img_widht)
                y = int(lm.y * img_height)
                # print(lm.x, lm.y)
                if id == 8:
                    mouse_x = int(screen_widht / img_widht * x)
                    mouse_y = int(screen_height / img_height * y)
                    cv2.circle(img,(x,y),10,(0,255,255))
                    pyautogui.moveTo(mouse_x, mouse_y)
                    x1 = x
                    y1 = y
                if id == 4:
                    x2 = x
                    y2 = y 
                    cv2.circle(img,(x,y),10,(0,255,255))
        dist = y2 - y1 
        # print(dist)
        if (dist < 40):
            pyautogui.click() 
            pyautogui.sleep(1)  
            print("click")
    cv2.imshow("Hand Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
