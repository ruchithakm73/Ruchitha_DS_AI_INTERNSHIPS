import pandas as pd
data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
}

df = pd.DataFrame(data)
print(df)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])
print(df)

df = pd.get_dummies(df, columns=["Color"], drop_first=True)
print(df)