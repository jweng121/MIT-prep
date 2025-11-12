import pandas as pd
import numpy as np
from fastapi import FastAPI

app = FastAPI()

df_present = pd.read_csv("present_ev_incentives.csv")
df_after = pd.read_csv("after_ev_incentives.csv")

df_after["Percent change"] = df_after["Annual_Energy_Savings_(%)"] - df_present["Annual_Energy_Savings_(%)"]
df_after.drop("Annual_Energy_Savings_(%)", axis=1, inplace=True) 

df_after.to_json("ev_incentives_comparison.json", orient="records", indent=4)

@app.get("/ev-incentives")
def get_ev_incentives():
    return df_after.to_dict(orient="records")