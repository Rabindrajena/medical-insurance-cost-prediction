# Medical Insurance Cost Prediction

**Medical Insurance Cost Prediction** is a Streamlit web application that estimates the **annual medical insurance cost** of an individual based on input features such as age, BMI, smoking status, number of children, and region.  
This project demonstrates the use of **machine learning** combined with an **interactive web interface**.

---

## 🌐 Live Demo

👉 **Try the app here:**  
https://medical-insurance-cost-prediction-cjf4uptd44r6c93bjahsen.streamlit.app/

---

## 🧠 Project Overview

The goal of this project is to predict medical insurance costs using real-world personal and lifestyle features.  
A machine learning pipeline is trained using **scikit-learn** and deployed as a **Streamlit** web application for easy user interaction.

The complete model development and analysis are documented in the included Jupyter/Colab notebook.

---

## 🛠️ Features

- User-friendly web form for data input  
- Predicts estimated medical insurance cost  
- Fast and interactive UI using Streamlit  
- Pre-trained machine learning model loaded with joblib  

---

## 🧩 Technologies Used

- **Python 3.11**
- **Streamlit** – Web application framework  
- **scikit-learn** – Machine learning  
- **pandas** – Data manipulation  
- **NumPy** – Numerical computing  
- **joblib** – Model serialization  

---

## 📂 Repository Structure

medical-insurance-cost-prediction/
│
├── app.py # Streamlit application
├── requirements.txt # Python dependencies
├── runtime.txt # Python version for Streamlit Cloud
├── medical_insurance_pipeline.pkl # Trained ML pipeline
├── medical_insurance_cost_prediction.ipynb # Model training notebook
└── README.md # Project documentation


---

## 🚀 Getting Started (Local Setup)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Rabindrajena/medical-insurance-cost-prediction.git
cd medical-insurance-cost-prediction

### 2️⃣ Create a virtual environment (recommended)
python -m venv venv

### 3️⃣ Activate the virtual environment

**Windows**

venv\Scripts\activate

**macOS / Linux**

source venv/bin/activate

### 4️⃣ Install dependencies
pip install -r requirements.txt

### 5️⃣ Run the Streamlit app
streamlit run app.py

The app will open in your browser at:
http://localhost:8501

##📝 How to Use the App

**1.** Open the Streamlit interface

**2.** Enter age, BMI, sex, smoking status, number of children, and region

**3.** Click **Predict**

**4.** View the estimated medical insurance cost

## 📈 Model Training (Optional)

If you want to retrain the model, use the Jupyter notebook provided in the repository.

⚠️ Make sure the **scikit-learn version used for training matches** the version in requirements.txt to avoid compatibility issues.

### Save the model
import joblib
joblib.dump(pipeline, "medical_insurance_pipeline.pkl")

### Load the model in the app
model = joblib.load("medical_insurance_pipeline.pkl")

## ☁️ Deployment (Streamlit Cloud)

**1.** Push your project to GitHub

**2.** Go to https://streamlit.io/cloud

**3.** Create a new app and connect your repository

**4.** Ensure runtime.txt contains:

python-3.11
**5.** Deploy and share your app

## 📌 Notes
* This app uses a pre-trained model included in the repository

* Dependency versions are pinned for Streamlit Cloud compatibility

## 👨‍💻 Author
**Rabindra Jena**
GitHub: https://github.com/Rabindrajena

