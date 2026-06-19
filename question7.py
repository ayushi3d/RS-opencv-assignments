import cv2
import mediapipe as mp
import math

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

led_on = False
pinch_detected = False

while True:
    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        hand = result.multi_hand_landmarks[0]

        h, w, c = frame.shape

        # Thumb Tip (Landmark 4)
        thumb_x = int(hand.landmark[4].x * w)
        thumb_y = int(hand.landmark[4].y * h)

        # Index Tip (Landmark 8)
        index_x = int(hand.landmark[8].x * w)
        index_y = int(hand.landmark[8].y * h)

        cv2.circle(frame, (thumb_x, thumb_y), 10, (255, 0, 0), -1)
        cv2.circle(frame, (index_x, index_y), 10, (255, 0, 0), -1)

        distance = math.hypot(
            index_x - thumb_x,
            index_y - thumb_y
        )

        if distance < 30 and not pinch_detected:
            led_on = not led_on
            pinch_detected = True

        if distance > 40:
            pinch_detected = False

    # LED Indicator
    if led_on:
        cv2.circle(frame, (100, 100), 40, (0, 255, 0), -1)
        cv2.putText(
            frame,
            "ON",
            (75, 170),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )
    else:
        cv2.circle(frame, (100, 100), 40, (0, 0, 255), -1)
        cv2.putText(
            frame,
            "OFF",
            (65, 170),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    cv2.imshow("LED INDICATOR", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()