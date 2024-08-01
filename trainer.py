import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer.create()
path = "dataset"


def get_images_with_id(Path):
    images_path = [os.path.join(Path, f) for f in os.listdir(Path)]
    Faces = []
    ids = []
    for single_image_path in images_path:
        faceImg = Image.open(single_image_path).convert('L')
        faceNp = np.array(faceImg, np.uint8)
        id = int(os.path.split(single_image_path)[-1].split(".")[1])
        print(id)
        Faces.append(faceNp)
        ids.append(id)
        cv2.imshow("Training", faceNp)
        cv2.waitKey(10)
    return np.array(ids), Faces


ids, faces = get_images_with_id(path)
recognizer.train(faces, ids)
recognizer.save("recognizer/trainingdata.yml")
cv2.destroyAllWindows()
