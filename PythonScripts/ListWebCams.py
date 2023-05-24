import cv2

# Get the IDs of all available webcams
num_cameras = 0
camera_ids = []
while True:
    cap = cv2.VideoCapture(num_cameras)
    if not cap.read()[0]:
        break
    camera_ids.append(num_cameras)
    num_cameras += 1
    cap.release()

# Check if any webcams were found
if not camera_ids:
    print("No webcams found")
    exit()

# Print the IDs of all available webcams
print("Available webcams:")
for i, camera_id in enumerate(camera_ids):
    print(f"{i}: Webcam {camera_id}")

# Prompt the user to select a webcam
while True:
    choice = input("Select a webcam (enter the number): ")
    try:
        choice = int(choice)
        if choice in range(len(camera_ids)):
            break
    except ValueError:
        pass
    print("Invalid choice")

# Open the selected webcam
cap = cv2.VideoCapture(camera_ids[choice])

# Check if the webcam was successfully opened
if not cap.isOpened():
    print("Error opening webcam")
    exit()

# Loop to continuously read frames from the webcam
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Error reading frame")
        break

    # Show the frame in a window named "Webcam"
    cv2.imshow("Webcam", frame)

    # Wait for 5 milliseconds and check if the "ESC" key was pressed
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()