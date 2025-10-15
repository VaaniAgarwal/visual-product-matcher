🛒 Visual Product Matcher

A web-based application that allows users to find visually similar products using image-based matching. The system combines image feature extraction with a recommendation mechanism to help users discover similar products based on visual similarity.

---

🚀 Live Demo

Working Application URL: Deployment in progress (Render Hosting)
(The project can be run locally using the instructions below.)

---

📁 GitHub Repository

Source Code: https://github.com/VaaniAgarwal/visual-product-matcher

---

💡 Project Overview

Visual Product Matcher is a Flask-based web application that enables users to upload an image or enter an image URL to find visually similar items from an existing product catalog. It uses pre-extracted image features and similarity computation techniques to retrieve the most relevant matches efficiently.

The system can be useful for e-commerce and visual search applications, helping users discover alternative products that look similar to a reference image.

---

🧠 Approach 

This project integrates machine learning–based feature extraction and similarity search to match visually related products. Each catalog image is processed using a hybrid feature extraction model (combining color histograms and deep feature embeddings) to obtain numerical representations (feature vectors). These vectors are stored for efficient retrieval using cosine similarity.

When a user uploads an image or provides an image URL, the system extracts its feature vector and computes similarity scores with the stored catalog features. The top-matching items are displayed with similarity percentages and filtering options.

The web interface, built with Flask and responsive HTML templates, provides an intuitive experience for browsing, searching, and visual matching. Product details are stored in a PostgreSQL database, and the system is designed for scalable deployment using Render or similar platforms.

---

⚙️ Tech Stack

Frontend: HTML, CSS, Bootstrap

Backend: Python (Flask)

Database: PostgreSQL

Machine Learning: NumPy, scikit-learn, OpenCV, pickle

Deployment (Planned): Render (Free Hosting)

---

📸 Features

Upload or provide an image URL for product matching

Display top visually similar products

Filter results by similarity score

Product catalog browsing with search and category filters

Mobile responsive and clean UI

Modular and scalable backend design

---

🧩 Setup Instructions

Clone the repository
git clone https://github.com/VaaniAgarwal/visual-product-matcher.git

cd visual-product-matcher

Create a virtual environment
python -m venv venv
(On Windows) venv\Scripts\activate
(On Mac/Linux) source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Configure the database
You can use the default local PostgreSQL connection or set your own in config.py:
SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:5432/visual_matcher_db"

Run the application
python app.py

Open in browser
http://127.0.0.1:5000

---

🧪 Example Usage

Go to Visual Match page.

Upload an image (or paste an image URL).

View top 5 visually similar products with similarity scores.

Filter results dynamically using the similarity slider.

---

🧾 Deliverables

Working Application URL: Render Deployment in Progress

GitHub Repository: https://github.com/VaaniAgarwal/visual-product-matcher

Brief Write-up (Approach): Included in the README above (under 200 words)

---

👩‍💻 Author

Vaani Agarwal
🔗 [LinkedIn](https://www.linkedin.com/in/vaani-agarwal-learner/) | [GitHub](https://github.com/VaaniAgarwal) 