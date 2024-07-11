import cv2
import torch
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1

# Load FaceNet model
mtcnn = MTCNN(keep_all=True, device='cpu')
resnet = InceptionResnetV1(pretrained='vggface2').eval()

# Load the photo to compare with live cam
photo_path = 'project/public/images/pic2.jpeg'  # 사진의 경로를 입력하세요
photo = cv2.imread(photo_path)

# Function to extract face embeddings using FaceNet
def get_face_embedding(image):
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes, _ = mtcnn.detect(rgb_image)
    if boxes is not None:
        faces = mtcnn.extract(rgb_image, boxes, None)
        embeddings = resnet(faces)
        return embeddings
    else:
        return None

# Get face embedding for the photo
photo_embedding = get_face_embedding(photo)

if photo_embedding is None:
    print("No face detected in the photo.")
else:
    print("Face detected in the photo.")

# Start video capture from the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Get face embedding for the current frame
    frame_embedding = get_face_embedding(frame)

    if frame_embedding is not None and photo_embedding is not None:
        # Compare embeddings between the photo and the current frame
        distance = torch.norm(photo_embedding - frame_embedding, p=2).item()
        matching_rate = max(0, (1 - distance / 2) * 100)  # 유사도에서 매칭률 계산

        # 설정한 임계값 이상일 때 매칭 텍스트 표시
        if matching_rate > 90:  # 임계값을 설정합니다.
            text = f"Match: {matching_rate:.2f}%"
        else:
            text = f"Not a Match: {matching_rate:.2f}%"

        # Draw result text on the frame
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Live Cam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
