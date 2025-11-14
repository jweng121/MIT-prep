from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("data.csv")

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.get("/data")
def get_data():
    return df.to_dict(orient="records")

@app.get("/summary")
def summary():
    return {
        "columns": list(df.columns),
        "rows": len(df),
        "stats": df.describe().to_dict()
    }

#********** js code snippet **********

useEffect(() => {
  fetch("http://localhost:8000/data")
    .then(res => res.json())
    .then(data => setData(data));
}, []);

#********** for ml, in train.py **********
from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle

df = pd.read_csv("data.csv")

X = df[["feature1", "feature2"]]
y = df["target"]

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

#********** then load model **********

import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

@app.post("/predict")
def predict(input: InputData):
    x = np.array([[input.feature1, input.feature2]])
    y_pred = model.predict(x)
    return {"prediction": float(y_pred[0])}