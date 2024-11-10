# Multiple Disease Prediction System

This project is a Streamlit-based application designed to predict the likelihood of three diseases—diabetes, heart disease, and Parkinson's—based on user-inputted health metrics. It leverages pre-trained machine learning models to make predictions and provides personalized health recommendations using an AI-powered assistant. **Disclaimer: This tool does not provide medical advice and is intended for informational purposes only. Always consult healthcare professionals for medical advice.**

## Table of Contents
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Disclaimer](#disclaimer)

## Features
- **Disease Prediction**: Provides predictions for diabetes, heart disease, and Parkinson's based on health indicators.
- **AI Recommendations**: Generates personalized health guidance for users with positive diagnoses.
- **User-Friendly Interface**: Interactive UI built with Streamlit, allowing easy input of health metrics and model selection.

## Directory Structure
The project has the following structure:
```plaintext
Data Set/
    ├── diabetes.csv
    ├── heart.csv
    └── parkinsons.csv
Note Books/
    ├── diabetes.ipynb
    ├── heart.ipynb
    ├── parkinsons.ipynb
models/
    ├── diabetes_model.sav
    ├── heart_disease_model.sav
    └── parkinsons_model.sav
.gitignore
app.py
```

- **Data Set/**: Contains CSV files with relevant data for each disease.
- **Note Books/**: Jupyter notebooks for data exploration, model training, and evaluation.
- **models/**: Serialized machine learning models for each disease.
- **app.py**: The main Streamlit application file that loads models and serves the prediction interface.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rathnayaka00/multiple-disease-prediction-system.git
   cd multiple-disease-prediction-system
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv env
   source env/Scripts/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**:
   - Add your Google API key to `.streamlit/secrets.toml` to enable the AI assistant.
   - Example `.streamlit/secrets.toml`:
     ```toml
     [api_keys]
     google_api_key = "YOUR_GOOGLE_API_KEY"
     ```

## Usage

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```

2. **Select Disease Prediction**: Choose from diabetes, heart disease, or Parkinson's prediction models.

3. **Enter Health Metrics**: Input relevant health metrics for prediction.

4. **Get Prediction and Recommendations**: Click "Predict" to see the result and receive personalized recommendations if diagnosed.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Web framework for creating an interactive UI.
- **Machine Learning**: Models for predicting diabetes, heart disease, and Parkinson's.
- **Google Generative AI**: For generating personalized health recommendations.
- **Jupyter Notebooks**: For data exploration and model training.

## Disclaimer
This project is intended for informational purposes only and does not constitute medical advice. Always seek the guidance of qualified healthcare providers for any health concerns.

---

Copy and paste this content into your `README.md` file, and adjust the repository link as needed.
