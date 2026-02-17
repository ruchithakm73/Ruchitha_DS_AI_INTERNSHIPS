import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = {
    "Age": [22, 25, 30, 35, 40, 28, 32, 45, 50, 29],
    "Salary": [20000, 25000, 30000, 40000, 50000, 27000, 32000, 60000, 80000, 29000]
}

df = pd.DataFrame(data)

print("Original Data:\n")
print(df)

standard_scaler = StandardScaler()
df_standardized = df.copy()
df_standardized[["Age", "Salary"]] = standard_scaler.fit_transform(df[["Age", "Salary"]])

print("\nStandardized Data:\n")
print(df_standardized)

minmax_scaler = MinMaxScaler()
df_normalized = df.copy()
df_normalized[["Age", "Salary"]] = minmax_scaler.fit_transform(df[["Age", "Salary"]])

print("\nNormalized Data:\n")
print(df_normalized)

plt.figure(figsize=(15,5))

plt.subplot(1, 3, 1)
plt.hist(df["Salary"], bins=5)
plt.title("Original Salary")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.subplot(1, 3, 2)
plt.hist(df_standardized["Salary"], bins=5)
plt.title("Standardized Salary")
plt.xlabel("Standardized")
plt.ylabel("Frequency")

plt.subplot(1, 3, 3)
plt.hist(df_normalized["Salary"], bins=5)
plt.title("Normalized Salary")
plt.xlabel("Normalized")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()