import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

canvas = np.zeros((480, 640, 3), dtype=np.uint8)

xp, yp = 0, 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            h, w, c = frame.shape


            x = int(hand.landmark[8].x * w)
            y = int(hand.landmark[8].y * h)

            cv2.circle(frame, (x, y), 8, (255, 0, 255), -1)


            fingers = []


            fingers.append(
                1 if hand.landmark[8].y < hand.landmark[6].y else 0
            )
            fingers.append(
                1 if hand.landmark[12].y < hand.landmark[10].y else 0
            )
            fingers.append(
                1 if hand.landmark[16].y < hand.landmark[14].y else 0
            )
            fingers.append(
                1 if hand.landmark[20].y < hand.landmark[18].y else 0
            )


            cv2.putText(
                frame,
                str(fingers),
                (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )

            # DRAWING
            if fingers == [1, 0, 0, 0]:

                cv2.putText(
                    frame,
                    "DRAW",
                    (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                if xp == 0 and yp == 0:
                    xp, yp = x, y

                cv2.line(
                    canvas,
                    (xp, yp),
                    (x, y),
                    (0, 255, 0),
                    5
                )

                xp, yp = x, y

            # ERASER
            elif fingers == [1, 1, 1, 1]:

                cv2.putText(
                    frame,
                    "ERASER",
                    (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

                if xp == 0 and yp == 0:
                    xp, yp = x, y

                cv2.line(
                    canvas,
                    (xp, yp),
                    (x, y),
                    (0, 0, 0),
                    30
                )

                xp, yp = x, y

            #PAUSE
            else:

                cv2.putText(
                    frame,
                    "PAUSE",
                    (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 0),
                    2
                )

                xp, yp = 0, 0

    combined = cv2.add(frame, canvas)

    cv2.imshow("Virtual Drawing Board", combined)

    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite("drawing.png", canvas)
        print("Drawing Saved Successfully")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()