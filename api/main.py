from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from schemas import Patient
import pandas as pd
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(directory=BASE_DIR / "templates")

import pandas as pd
import joblib
app = FastAPI(title="Cancer Prediction API")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
model = joblib.load("cancer_model.pkl")



@app.post("/predict")
def predict(patient: Patient):

    new_data = pd.DataFrame({
        "Age": [patient.Age],
        "Air_Pollution": [patient.Air_Pollution],
        "Alcohol_Use": [patient.Alcohol_Use],
        "Smoking": [patient.Smoking],
        "Obesity_Level": [patient.Obesity_Level]
    })

    prediction = model.predict(new_data)

    return {
        "prediction": prediction[0]
    }

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

