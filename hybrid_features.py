import numpy as np
import cv2
import os
import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing import image

model = VGG16(weights='imagenet', include_top=False, pooling='avg')

def extract_cnn_features(img_path):
    try:
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        expanded_img_array = np.expand_dims(img_array, axis=0)
        preprocessed_img = preprocess_input(expanded_img_array) 
        features = model.predict(preprocessed_img, verbose=0)
        return features.flatten()
    except Exception as e:
        print(f"⚠️ CNN feature extraction failed for {img_path}: {e}")
        return np.zeros(512)

def extract_color_histogram(img_path, bins=(8, 8, 8)):
    abs_path = os.path.abspath(img_path)
    img = cv2.imread(abs_path)
    if img is None:
        print(f"⚠️ Unable to load image (None): {abs_path}")
        return np.zeros(bins[0] * bins[1] * bins[2])
    try:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([img], [0, 1, 2], None, bins, [0, 180, 0, 256, 0, 256])
        cv2.normalize(hist, hist)   
        return hist.flatten()
    except Exception as e:
        print(f"⚠️ Color histogram failed for {img_path}: {e}")
        return np.zeros(bins[0] * bins[1] * bins[2])

def extract_hybrid_features(img_path):
    cnn_features = extract_cnn_features(img_path)
    color_features = extract_color_histogram(img_path)
    hybrid_vector = np.concatenate([cnn_features * 0.7, color_features * 0.3])
    return hybrid_vector