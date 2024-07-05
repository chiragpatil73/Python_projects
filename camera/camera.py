import cv2
import pyautogui
roi_top, roi_bottom, roi_left, roi_right = 100, 300, 100, 300
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    frame = cv2.flip(frame, 1)

    roi = frame[roi_top:roi_bottom, roi_left:roi_right]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    # Use thresholding to segment the hand region
    _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the threshold image
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the maximum area (assuming it's the hand)
    if contours:
        hand_contour = max(contours, key=cv2.contourArea)

        # Get the centroid of the hand contour
        M = cv2.moments(hand_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # Map the centroid coordinates to the full frame
            mapped_x = int(cx * (1920 / 200))  # Change 1920 to your screen width
            mapped_y = int(cy * (1080 / 200))  # Change 1080 to your screen height

            # Move the mouse cursor to the mapped coordinates
            pyautogui.moveTo(mapped_x, mapped_y)

    # Display the frame
    cv2.imshow("Finger Control", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
