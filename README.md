# 🌾 Explainable AI for Crop Recommendation, Yield Forecasting and Rainfall Prediction in Smart Agriculture

## 📌 Project Overview

Agriculture is a critical sector that directly impacts food security and economic stability. This project presents a smart agriculture system powered by **Artificial Intelligence (AI)** and **Explainable AI (XAI)** techniques to assist farmers in making informed decisions.

The system integrates three major functionalities:

* 🌱 Crop Recommendation
* 📈 Yield Forecasting
* 🌧️ Rainfall Prediction

Unlike traditional systems, this project not only provides predictions but also explains **why** a particular decision is made, improving transparency and trust among users.

---

## 🎯 Objectives

* To recommend suitable crops based on soil and environmental conditions
* To predict crop yield using historical and environmental data
* To forecast rainfall using machine learning models
* To provide explainable insights using XAI techniques
* To improve decision-making in smart agriculture

---

## 🧠 Technologies Used

* Python
* Machine Learning (ML)
* Explainable AI (XAI)
* Flask / Streamlit (Frontend & Backend)
* Libraries:

  * NumPy
  * Pandas
  * Scikit-learn
  * TensorFlow / Keras
  * XGBoost
  * Matplotlib / Seaborn

---

## ⚙️ System Architecture

The system consists of the following modules:

1. **Data Collection Module**

   * Soil data (N, P, K, pH)
   * Weather data (temperature, humidity, rainfall)

2. **Data Preprocessing**

   * Cleaning missing values
   * Feature scaling
   * Data normalization

3. **Model Training**

   * Crop Recommendation → Classification models
   * Yield Prediction → Regression models
   * Rainfall Prediction → Time-series / regression

4. **Explainable AI Module**

   * SHAP (Shapley Additive Explanations)
   * Feature importance visualization

5. **User Interface**

   * Web-based interface for user inputs and results

---

## 🔍 Features

* ✔ Smart crop recommendation based on soil nutrients
* ✔ Accurate yield prediction using ML models
* ✔ Rainfall prediction for better planning
* ✔ Explainable outputs (why the model predicted this)
* ✔ User-friendly interface

---

## 📊 Machine Learning Models

* Random Forest
* XGBoost
* Artificial Neural Networks (ANN)
* Linear Regression

---

## 🧪 Explainable AI Techniques

This project uses Explainable AI methods to interpret model predictions:

* SHAP values to show feature importance
* Visual explanations for decision-making
* Transparent prediction reasoning

---

## 🖥️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Mohan-vamsi855/Mohan-Final-Year-Project.git
cd Mohan-Final-Year-Project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

OR (if using Streamlit):

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Mohan-Final-Year-Project/
│
├── CODE/
│   ├── BACKEND CODE/
│   ├── FRONTEND CODE/
│
├── requirements.txt
├── runtime.txt
├── README.md
```

---

## 📈 Results & Discussion

The system demonstrates high accuracy in:

* Crop recommendation based on soil data
* Yield prediction using trained ML models
* Rainfall forecasting

The use of Explainable AI helps users understand:

* Which features influenced predictions
* Why a particular crop is recommended

---

## 🚀 Future Scope

* Integration with IoT sensors for real-time data
* Mobile application for farmers
* Satellite data integration
* Advanced deep learning models
* Multi-language support

---

## ⚠️ Limitations

* Depends on dataset quality
* Requires internet for deployment
* Model performance varies by region

---

## 🤝 Contribution

Contributions are welcome!
Feel free to fork the repository and submit pull requests.

---

## 📜 License

This project is for educational purposes.

---

## 👨‍💻 Author

**Mohan Vamsi**
Final Year Project – Smart Agriculture using AI & XAI

---

## ⭐ Acknowledgements

* Machine Learning community
* Open-source datasets
* Research papers on Smart Agriculture

---
