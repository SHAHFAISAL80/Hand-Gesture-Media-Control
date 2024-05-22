import cv2
import mediapipe as mp
import pyautogui
import time

# Function to count the number of fingers based on landmark positions
def count_fingers(lst):
    count = 0

    threshold = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > threshold:
        count += 1

    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > threshold:
        count += 1

    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > threshold:
        count += 1

    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > threshold:
        count += 1

    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
        count += 1

    return count

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize mediapipe hands module
drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

start_init = False
prev = -1

task_text = ""  # Initialize task text

while True:
    end_time = time.time()
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    # Process the frame with mediapipe hands
    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
        hand_keyPoints = res.multi_hand_landmarks[0]
        finger_count = count_fingers(hand_keyPoints)

        if not(prev == finger_count):
            if not(start_init):
                start_time = time.time()
                start_init = True
            elif (end_time - start_time) > 0.2:
                if finger_count == 1:
                    pyautogui.press("right")  # Press right arrow key for forward skip
                    task_text = "Forward Skip"
                elif finger_count == 2:
                    pyautogui.press("left")  # Press left arrow key for backward skip
                    task_text = "Backward Skip"
                elif finger_count == 3:
                    pyautogui.press("volumeup")  # Press volume up key for increasing volume
                    task_text = "Volume Up"
                elif finger_count == 4:
                    pyautogui.press("volumedown")  # Press volume down key for decreasing volume
                    task_text = "Volume Down"
                elif finger_count == 5:
                    pyautogui.press("space")  # Press spacebar for pause/play
                    task_text = "Pause/Play"

                prev = finger_count
                start_init = False

        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

    # Draw task text inside a box
    cv2.rectangle(frm, (10, 10), (300, 60), (0, 0, 0), -1)  # Draw a filled black rectangle
    cv2.putText(frm, task_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
