from pydantic import BaseModel

class Patient(BaseModel):
    Age: float
    Air_Pollution: float
    Alcohol_Use: float
    Smoking: float
    Obesity_Level: float