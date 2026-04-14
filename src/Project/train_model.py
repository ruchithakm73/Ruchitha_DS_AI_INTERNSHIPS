import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score
from sklearn.preprocessing import StandardScaler
import pickle
import warnings
warnings.filterwarnings('ignore')

# Load dataset
data = pd.read_csv("hospital_readmission_risk_dataset_2026_v1_18000rows (1).csv")

# Clean column names (remove spaces + fix format)
data.columns = data.columns.str.strip().str.replace(" ", "_")

print("=" * 70)
print("🏥 HOSPITAL READMISSION RISK PREDICTION MODEL (85% ACCURACY TARGET)")
print("=" * 70)

# Select relevant features for readmission prediction
# Remove non-predictive columns (dates, IDs, disposition)
exclude_cols = ['Patient_ID', 'Admission_Date', 'Discharge_Date', 'Discharge_Disposition', 'Readmitted_Within_30_Days', 'Room_No', 'Bed_No']
feature_cols = [col for col in data.columns if col not in exclude_cols]

X = data[feature_cols].copy()
y = data['Readmitted_Within_30_Days'].copy()

# Encode categorical variables
categorical_cols = X.select_dtypes(include=['object']).columns
X_encoded = X.copy()
for col in categorical_cols:
    X_encoded[col] = pd.Categorical(X_encoded[col]).codes

X = X_encoded
feature_cols = list(X.columns)

print(f"\n📊 Dataset Info:")
print(f"   Total samples: {len(data)}")
print(f"   Features: {len(feature_cols)}")
print(f"   Target variable: Readmitted_Within_30_Days")
print(f"   Readmission rate: {y.sum()/len(y)*100:.2f}%")

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"\n🔄 Data Split:")
print(f"   Training samples: {len(X_train)}")
print(f"   Testing samples: {len(X_test)}")

# Standardize features (for future use in other models)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Use class-weighted Random Forest for better accuracy
print(f"\n🤖 Training Advanced Random Forest Model...")

best_model = RandomForestClassifier(
    n_estimators=250,
    max_depth=20,
    min_samples_split=2,
    min_samples_leaf=1,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)
best_model.fit(X_train, y_train)

# Make predictions
y_pred = best_model.predict(X_test)
y_pred_proba = best_model.predict_proba(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba[:, 1])
cm = confusion_matrix(y_test, y_pred)

print(f"\n✅ MODEL PERFORMANCE - RESULTS:")
print(f"   Accuracy:  {accuracy*100:.2f}% 🎯")
print(f"   Precision: {precision*100:.2f}%")
print(f"   Recall:    {recall*100:.2f}%")
print(f"   F1-Score:  {f1*100:.2f}%")
print(f"   ROC-AUC:   {roc_auc*100:.2f}%")
print(f"\n📈 Confusion Matrix:")
print(f"   True Negatives:  {cm[0,0]:>4}")
print(f"   False Positives: {cm[0,1]:>4}")
print(f"   False Negatives: {cm[1,0]:>4}")
print(f"   True Positives:  {cm[1,1]:>4}")

# Calculate sensitivity and specificity
sensitivity = cm[1,1] / (cm[1,1] + cm[1,0])
specificity = cm[0,0] / (cm[0,0] + cm[0,1])
print(f"\n🔍 Additional Metrics:")
print(f"   Sensitivity (True Positive Rate): {sensitivity*100:.2f}%")
print(f"   Specificity (True Negative Rate): {specificity*100:.2f}%")

# Feature importance for Gradient Boosting
feature_importance = pd.DataFrame({
    'feature': feature_cols,
    'importance': best_model.feature_importances_
}).sort_values('importance', ascending=False)

print(f"\n🎯 Top 10 Most Important Features:")
for idx, (feat, imp) in enumerate(zip(feature_importance['feature'].head(10), feature_importance['importance'].head(10)), 1):
    print(f"   {idx:2d}. {feat:30s}: {imp*100:6.2f}%")

# Save model, feature columns, and scaler
pickle.dump(best_model, open("model.pkl", "wb"))
pickle.dump(feature_cols, open("feature_cols.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

print(f"\n💾 Model, features, and scaler saved successfully!")
print("=" * 70)
print(f"✨ Accuracy Achieved: {accuracy*100:.2f}%")
print("=" * 70)


