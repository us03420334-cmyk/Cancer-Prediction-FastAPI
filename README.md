# Cancer Prediction using Machine Learning and FastAPI

## Project Description

This project predicts the likelihood of cancer based on patient health information. The machine learning model is trained using patient data and deployed as a web application using FastAPI.

## Features

* Predicts cancer using a trained machine learning model
* User-friendly web interface
* FastAPI backend
* HTML, CSS, and JavaScript frontend
* Interactive API documentation with Swagger UI

## Input Features

The model uses the following input parameters:

* Age
* Air Pollution
* Alcohol Use
* Smoking
* Obesity Level

## Technologies Used

* Python
* FastAPI
* Pandas
* Scikit-learn
* Joblib
* Jinja2
* HTML
* CSS
* JavaScript

## Project Structure

```
cancer_prediction/
│
├── api/
│   ├── main.py
│   ├── schemas.py
│   └── cancer_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Navigate to the API folder:

```bash
cd api
```

4. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

5. Open your browser and visit:

```
http://127.0.0.1:8000
```

## API Documentation

Swagger UI is available at:

```
http://127.0.0.1:8000/docs
```

## Author

Umer Sultan
