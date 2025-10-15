# 🛒 Visual Product Matcher

A web-based application that allows users to find visually similar products using image-based matching. The system combines image feature extraction with a recommendation mechanism to help users discover similar products based on visual similarity.

---

## 🚀 Live Demo

**Working Application URL:** _Currently not deployed due to resource limitations (can run locally)_
The project runs fully on local machines following the setup instructions below.

---

## 📁 GitHub Repository

**Source Code:** [https://github.com/VaaniAgarwal/visual-product-matcher](https://github.com/VaaniAgarwal/visual-product-matcher)

---

## 💡 Project Overview

Visual Product Matcher is a Flask-based web application that enables users to upload an image or enter an image URL to find visually similar items from an existing product catalog. It uses pre-extracted image features and similarity computation techniques to retrieve the most relevant matches efficiently.

The system can be useful for e-commerce and visual search applications, helping users discover alternative products that look similar to a reference image.

---

## 🧠 Approach 

This project integrates machine learning–based feature extraction and similarity search to match visually related products. Each catalog image is processed using a hybrid feature extraction model (combining color histograms and deep feature embeddings) to obtain numerical representations (feature vectors). These vectors are stored for efficient retrieval using cosine similarity.

When a user uploads an image or provides an image URL, the system extracts its feature vector and computes similarity scores with the stored catalog features. The top-matching items are displayed with similarity percentages and filtering options.

The web interface, built with Flask and responsive HTML templates, provides an intuitive experience for browsing, searching, and visual matching. Product details are stored in a PostgreSQL database.

⚠️ Note: Due to model size, online deployment on free hosting platforms is not currently feasible.

---

## ⚙️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python (Flask)
- **Database:** PostgreSQL
- **Machine Learning:** NumPy, scikit-learn, OpenCV, pickle

---

## 📸 Features

- Upload or provide an image URL for product matching
- Display top visually similar products
- Filter results by similarity score
- Product catalog browsing with search and category filters
- Mobile responsive and clean UI

---

## 🧩 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/VaaniAgarwal/visual-product-matcher.git

cd visual-product-matcher
```

### 2. Create a virtual environment
```bash
python -m venv venv
(On Windows) venv\Scripts\activate
(On Mac/Linux) source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the database
You can use the default local PostgreSQL connection or set your own in config.py:
```bash
SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:5432/visual_matcher_db"
```

### 5. Run the application
```bash
python app.py
```

### 6. Open in browser
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Example Usage

1. Go to Visual Match page.
2. Upload an image (or paste an image URL).
3. View top 5 visually similar products with similarity scores.
4. Filter results dynamically using the similarity slider.

---

## 🧾 Deliverables

- GitHub Repository: [https://github.com/VaaniAgarwal/visual-product-matcher](https://github.com/VaaniAgarwal/visual-product-matcher)
- Demo: Run locally as described above
- Brief Write-up (Approach): Included in the README above (under 200 words)

---

## 👩‍💻 Author

**Vaani Agarwal**
🔗 [LinkedIn](https://www.linkedin.com/in/vaani-agarwal-learner/) | [GitHub](https://github.com/VaaniAgarwal) 