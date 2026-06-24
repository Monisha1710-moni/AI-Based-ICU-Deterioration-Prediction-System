
# ICU Deterioration Prediction System

## Overview

An AI-powered early warning system that predicts the risk of ICU patient deterioration using Machine Learning.

The system analyzes critical patient parameters and provides risk predictions with confidence scores to assist healthcare professionals in making timely decisions.

---

## Features

- ICU deterioration risk prediction
- XGBoost Machine Learning model
- Confidence score generation
- SHAP explainability support
- Interactive Flask web application
- User-friendly interface

---

## Tech Stack

- Python
- Flask
- XGBoost
- Pandas
- NumPy
- Scikit-learn
- SHAP
- HTML
- CSS
- JavaScript

---

## Input Features

- Age
- Glucose
- Heart Rate (HR)
- Temperature
- Systolic Blood Pressure (SysABP)
- Respiratory Rate (RespRate)

---

## Project Structure

AI-Based-ICU-Deterioration-Prediction-System/
│
├── app.py
├── model.pkl
├── requirements.txt
├── icu_deterioration_prediction.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   ├── hero-bg.jpg
│   ├── hero-bg2.avif
│   └── shap_summary.png
│
└── README.md

## How to Run

1. Clone the Repository

git clone https://github.com/Monisha1710-moni/AI-Based-ICU-Deterioration-Prediction-System.git

2. Navigate to the Project Folder

cd AI-Based-ICU-Deterioration-Prediction-System

3. Install Dependencies

pip install -r requirements.txt

4. Run the Flask Application

python app.py

### 5. Open in Browser

[http://127.0.0.1:5000](http://127.0.01:5000)

Future Enhancements

- Real-time patient monitoring
- Early warning alert system
- Hospital database integration
- Cloud deployment
- Explainable AI enhancements
- Continuous patient data analysis
- Automated risk notifications

Author
**Monisha K**
Computer Science and Engineering (Data Science)
Dayananda Sagar University
