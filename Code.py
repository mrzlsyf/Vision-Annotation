# Detect eyes and write letters above the eyes
import cv2

# HAAR Cascade initialization to detect eyes
cek_mata = cv2.CascadeClassifier('eye-detect.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, v = cap.read()
    v = cv2.flip(v, 1)

    # find eye coordinates
    hasil = cek_mata.detectMultiScale(v)

    # If found it, make a box and write on it.
    for x, y, l, t in hasil:
      cv2.rectangle(v, (x, y), (x+l, y+t), (0, 0, 255), 4)
      cv2.putText(v, 'PeiJal', (x, y-t//2), 0, 0.5, (0, 255, 0), 2)

    cv2.imshow('mrs', v)

    if cv2.waitKey(1)== ord('q'):
        break

cv2.destroyAllWindows()
cap.release()


# ---------------------------------------------------------------- #
# Writes the sequence of numbers in sequence on the detected chess board
import cv2

# Initialize the stopping criteria to refine the chessboard corner discovery
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, v = cap.read()
    if not ret:
        print("Gagal membaca frame.")
        break

    # Flip the frame horizontally
    v = cv2.flip(v, 1)

    # Look for the corners of the chessboard
    stat, corner = cv2.findChessboardCorners(v, (7, 6), None)

    # If corners are found, refine them
    if stat:
        # Refine the corner locations
        corner = cv2.cornerSubPix(cv2.cvtColor(v, cv2.COLOR_BGR2GRAY), corner, (11, 11), (-1, -1), criteria)
        
        # Convert corners to integer (optional)
        corner_int = corner.astype(int)

        # Show the results of the corners
        for c, _ in enumerate(corner_int):
            cv2.putText(v, str(c), tuple(_[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('JalJal', v)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
cap.release()