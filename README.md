# Medical Insurance Cost Prediction

**Medical Insurance Cost Prediction** is a Streamlit web application that estimates the **annual medical insurance cost** of an individual based on input features such as age, BMI, smoking status, number of children, and region.  
This project demonstrates the use of **machine learning** combined with an **interactive web interface**.

---


## Detailed Analysis
A complete exploratory data analysis, feature engineering, model training,
and evaluation is documented in the notebook: 📔[Colab Notebook - Full ML Blog](https://colab.research.google.com/github/Rabindrajena/medical-insurance-cost-prediction/blob/main/Medical_Insurance_Cost_Prediction.ipynb)

---

## 🌐 Live Demo

👉 **Try the app here:**   https://medical-insurance-cost-prediction-cjf4uptd44r6c93bjahsen.streamlit.app/

---

## 📷Screenshot

<img width="1147" height="813" alt="Screenshot 2026-01-29 223650" src="https://github.com/user-attachments/assets/8acb7b60-2eaf-4931-a790-0b214a3e4d72" />

---

## 🎥Live demo

![ScreenRecording2026-02-09014526-ezgif com-optimize](https://github.com/user-attachments/assets/4ba6ba2b-d2b0-46b5-b7b3-f6023ef31139)

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

`medical-insurance-cost-prediction/`

│

├── `medical_insurance_cost_prediction.ipynb` # Created using colab

├── `README.md` # Project documentation

├── `app.py` # Streamlit application

├── `medical.csv` # CSV file

├── `medical_insurance_cost_prediction.ipynb` # Model training notebook

├── `medical_insurance_pipeline.pkl` # Trained ML pipeline

├── `requirements.txt` # Python dependencies

└── `runtime.txt` # Python version for Streamlit Cloud

---

## 🚀 Getting Started (Local Setup)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Rabindrajena/medical-insurance-cost-prediction.git
cd medical-insurance-cost-prediction
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

The app will open in your browser at: http://localhost:8501

---

## 📝 How to Use the App

**1.** Open the Streamlit interface

**2.** Enter age, BMI, sex, smoking status, number of children, and region

**3.** Click **Predict**

**4.** View the estimated medical insurance cost

## 📈 Model Training (Optional)

If you want to retrain the model, use the Jupyter notebook provided in the repository.

⚠️ Make sure the **scikit-learn version used for training matches** the version in `requirements.txt` to avoid compatibility issues.

### Save the model

```bash
import joblib
joblib.dump(pipeline, "medical_insurance_pipeline.pkl")
```

### Load the model in the app

```bash
model = joblib.load("medical_insurance_pipeline.pkl")
```

## ☁️ Deployment (Streamlit Cloud)

**1.** Push your project to GitHub

**2.** Go to https://streamlit.io/cloud

**3.** Create a new app and connect your repository

**4.** Ensure `runtime.txt` contains:

`python-3.11`
**5.** Deploy and share your app

## 📌 Notes
* This app uses a pre-trained model included in the repository

* Dependency versions are pinned for Streamlit Cloud compatibility

## 👨‍💻 Author
**Rabindra Jena** [GitHub](https://github.com/Rabindrajena)

