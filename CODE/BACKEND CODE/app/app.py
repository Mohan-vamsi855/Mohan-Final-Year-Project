import os
import numpy as np
from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from lime.lime_tabular import LimeTabularExplainer
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load model and scaler
ann_model = tf.keras.models.load_model("ann_model.h5")
scaler = joblib.load('scaler.pkl')

# Define feature names
feature_names = [
    "Location", "MinTemp", "MaxTemp", "Rainfall", "Evaporation", "Sunshine", 
    "WindGustSpeed", "WindSpeed9am", "WindSpeed3pm", "Humidity9am", "Humidity3pm",
    "Pressure9am", "Pressure3pm", "Cloud9am", "Cloud3pm", "Temp9am", "Temp3pm", 
    "RISK_MM"
]

# Route: Homepage
@app.route("/")
def index():
    return render_template("index.html")

# Route: Prediction
@app.route("/predict", methods=["POST"])
def predict():
    # Parse user input
    user_input = [float(request.form.get(feature)) for feature in feature_names]
    input_scaled = scaler.transform(np.array(user_input).reshape(1, -1))
    
    # Prediction
    prediction_prob = ann_model.predict(input_scaled).ravel()[0]
    prediction_label = "Rain (1)" if prediction_prob > 0.5 else "No Rain (0)"
    
    # Suggestions
    suggestion = ("Rain is expected tomorrow. It's advisable to carry an umbrella, avoid outdoor activities, "
                  "and ensure your home is protected from potential water accumulation.") if prediction_label == "Rain (1)" else (
                  "No rain is forecasted tomorrow. Engage in outdoor activities, but stay prepared for sudden changes.")
    
    return render_template("result.html", prediction_label=prediction_label,
                           prediction_prob=round(prediction_prob, 2),
                           suggestion=suggestion, user_input=user_input)

# Route: Explanation
@app.route("/explain", methods=["POST"])
def explain():
    user_input = [float(value) for value in request.form.getlist('user_input')]
    
    def predict_fn(data):
        scaled_data = scaler.transform(data)
        prob_positive = ann_model.predict(scaled_data).ravel()
        prob_negative = 1 - prob_positive
        return np.column_stack((prob_negative, prob_positive))
    
    explainer = LimeTabularExplainer(
        training_data=X_train_scaled,
        feature_names=feature_names,
        class_names=["No Rain (0)", "Rain (1)"],
        mode="classification"
    )
    
    explanation = explainer.explain_instance(
        data_row=np.array(user_input),
        predict_fn=predict_fn,
        num_features=len(feature_names)
    )
    
    explanation.save_to_file("static/lime_explanation/explanation.html")
    return render_template("explanation.html", explanation_path="static/lime_explanation/explanation.html")

if __name__ == "__main__":
    app.run(debug=True)
