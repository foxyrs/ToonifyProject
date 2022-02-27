# from https://github.com/rolux

import os
import sys
import bz2
from tensorflow.keras.utils import get_file
from ffhq_dataset.face_alignment import image_align
from ffhq_dataset.landmarks_detector import LandmarksDetector
from pathlib import Path

LANDMARKS_MODEL_URL = 'http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2'
#LANDMARKS_MODEL_URL = Path(__file__).resolve().parent.parent/"../static/libs/shape_predictor_68_face_landmarks.dat.bz2"

def setup():
    landmarks_model_path = unpack_bz2(get_file('shape_predictor_68_face_landmarks.dat.bz2',
                                               LANDMARKS_MODEL_URL, cache_subdir='temp'))
    #  landmarks_model_path = unpack_bz2(Path(__file__).resolve().parent.parent/"../static/libs/shape_predictor_68_face_landmarks.dat.bz2")
    RAW_IMAGES_DIR = Path(__file__).resolve().parent.parent/"stylegan2/raw" #sys.argv[1]
    ALIGNED_IMAGES_DIR = Path(__file__).resolve().parent.parent/"stylegan2/aligned"#sys.argv[2]

    landmarks_detector = LandmarksDetector(landmarks_model_path)
    for img_name in [x for x in os.listdir(RAW_IMAGES_DIR) if x[0] not in '._']:
        raw_img_path = os.path.join(RAW_IMAGES_DIR, img_name)
        for i, face_landmarks in enumerate(landmarks_detector.get_landmarks(raw_img_path), start=1):
            face_img_name = '%s_%02d.png' % (os.path.splitext(img_name)[0], i)
            aligned_face_path = os.path.join(ALIGNED_IMAGES_DIR, face_img_name)
            os.makedirs(ALIGNED_IMAGES_DIR, exist_ok=True)
            image_align(raw_img_path, aligned_face_path, face_landmarks)

def unpack_bz2(src_path):
    data = bz2.BZ2File(src_path).read()
    dst_path = src_path[:-4]
    with open(dst_path, 'wb') as fp:
        fp.write(data)
    return dst_path


