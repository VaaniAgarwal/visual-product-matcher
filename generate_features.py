import os
import pickle
import numpy as np
from hybrid_features import extract_hybrid_features

IMAGE_DIR = "static/images"
FEATURES_FILE = "data/image_features.pkl"

os.makedirs("data", exist_ok=True)

features = {}
for img_name in os.listdir(IMAGE_DIR):
    if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(IMAGE_DIR, img_name)
        print(f"Extracting hybrid features for: {img_name}")
        try:
            vector = extract_hybrid_features(img_path)
            if vector is not None and np.any(vector):
                features[img_name] = vector
            else:
                print(f"⚠️ Skipped {img_name}: Empty features")
        except Exception as e:
            print(f"⚠️ Error processing {img_name}: {e}")

with open(FEATURES_FILE, 'wb') as f:
    pickle.dump(features, f)    

print(f"✅ Hybrid features saved successfully! ({len(features)} images processed)")