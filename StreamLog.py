import cv2
from ultralytics import YOLO
from datetime import datetime

model = YOLO("/home/rangertau/Documents/CNN/Weights/FPCS-greyscale-merged-v1.pt", verbose=True)

video_path = "/home/rangertau/Documents/CNN/Videos/peachersmill.mp4"


cap = cv2.VideoCapture(video_path)

sampling_interval = 0.25   #0.25 seconds

fps = cap.get(cv2.CAP_PROP_FPS)
frames_to_skip = int(fps*sampling_interval)

frame_count = 0

while cap.isOpened():

	success, frame = cap.read()
	
	# Resize the frame to a smaller size
	frame = cv2.resize(frame, (640, 360))  # Reduce to a lower resolution
	
	if success:
		if frame_count % frames_to_skip == 0:
			results = model(frame)
			print(f"Time: {datetime.now()}")
			#annotated_frame = results[0].plot()
			#cv2.imshow("YOLO Inference", annotated_frame)
		frame_count += 1
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break
	else:
		break
		
cap.release()
cv2.destroyAllWindows()



