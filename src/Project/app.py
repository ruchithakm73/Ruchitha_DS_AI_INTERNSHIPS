from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and feature columns
model = pickle.load(open("model.pkl", "rb"))
feature_cols = pickle.load(open("feature_cols.pkl", "rb"))
data = pd.read_csv("hospital_readmission_risk_dataset_2026_v1_18000rows (1).csv")

# Clean column names
data.columns = data.columns.str.strip().str.replace(" ", "_")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/lookup', methods=['POST'])
def lookup():
    patient_id_str = request.form.get('patient_id')
    
    if not patient_id_str:
        return render_template("index.html", error="Please provide the patient ID.")
    
    try:
        patient_id = int(patient_id_str)
    except ValueError:
        return render_template("index.html", error="Patient ID must be a valid number.")
    
    # Filter data by patient ID
    patient = data[data['Patient_ID'] == patient_id]
    
    if patient.empty:
        return render_template("index.html", error="No patient found with the given patient ID.")
    
    # Take the first match
    patient_row = patient.iloc[0]
    patient_details = patient_row.to_dict()
    
    # Prepare data for prediction
    X_patient_raw = patient_row[feature_cols].copy()
    
    # Convert to DataFrame for encoding
    X_patient_df = pd.DataFrame([X_patient_raw])
    
    # Encode categorical columns
    categorical_cols = X_patient_df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        X_patient_df[col] = pd.Categorical(X_patient_df[col], categories=pd.Categorical(data[col]).categories).codes
    
    X_patient = X_patient_df.values.reshape(1, -1)
    
    # Make prediction
    risk_prediction = model.predict(X_patient)[0]
    risk_probability = model.predict_proba(X_patient)[0]
    
    # Risk level
    risk_level = "HIGH RISK 🚨" if risk_prediction == 1 else "LOW RISK ✅"
    risk_percentage = (risk_probability[1] * 100)
    
    patient_details['risk_level'] = risk_level
    patient_details['risk_percentage'] = f"{risk_percentage:.1f}%"
    patient_details['recommendation'] = get_recommendation(risk_prediction, patient_row)
    
    return render_template("result.html", patient_details=patient_details)

def get_recommendation(risk_level, patient_row):
    """Generate actionable recommendations based on risk factors"""
    recommendations = []
    
    if risk_level == 1:  # High risk
        recommendations.append("🔴 URGENT: Schedule early follow-up appointment within 48 hours")
        
        if patient_row.get('Comorbidity_Index', 0) >= 3:
            recommendations.append("🏥 Multiple comorbidities detected - Coordinate with specialists")
        
        if patient_row.get('High_Risk_Medication_Flag', 0) == 1:
            recommendations.append("💊 High-risk medications - Ensure close medication monitoring")
        
        if patient_row.get('Severity_Score', 0) >= 7:
            recommendations.append("⚠️ High severity condition - Consider extended monitoring")
        
        if patient_row.get('Length_of_Stay', 0) > 10:
            recommendations.append("📋 Long hospitalization - Enhanced discharge planning needed")
    else:  # Low risk
        recommendations.append("✅ Standard discharge protocol - Regular follow-up in 2 weeks")
        recommendations.append("📞 Provide contact information for patient support services")
    
    return recommendations

if __name__ == "__main__":
    app.run(debug=True, port=5001)

