import os
import pickle
import streamlit as st
import google.generativeai as genai

if 'google_api_key' not in st.secrets['api_keys']:
    st.error('Google API key not found. Please add it to .streamlit/secrets.toml')
    st.stop()

genai.configure(api_key=st.secrets['api_keys']['google_api_key'])

model = genai.GenerativeModel('gemini-pro')

def get_medical_assistance(disease_type, user_inputs):
    if disease_type == 'Diabetes Prediction':
        prompt = f"""As a medical assistant, provide helpful recommendations for someone who has been diagnosed with diabetes. 
        Their details are:
        - Glucose Level: {user_inputs[1]}
        - Blood Pressure: {user_inputs[2]}
        - BMI: {user_inputs[5]}
        - Age: {user_inputs[7]}
        
        Please provide:
        1. Immediate steps they should take
        2. Lifestyle modifications
        3. Types of medical professionals they should consult
        4. Warning signs to watch for
        Important: Include a clear disclaimer that this is not medical advice and they should consult healthcare professionals."""
    
    elif disease_type == 'Heart Disease Prediction':
        prompt = f"""As a medical assistant, provide helpful recommendations for someone who has been diagnosed with heart disease. 
        Their details are:
        - Age: {user_inputs[0]}
        - Blood Pressure: {user_inputs[3]}
        - Cholesterol: {user_inputs[4]}
        - Max Heart Rate: {user_inputs[7]}
        
        Please provide:
        1. Immediate steps they should take
        2. Lifestyle modifications
        3. Types of medical professionals they should consult
        4. Warning signs to watch for
        Important: Include a clear disclaimer that this is not medical advice and they should consult healthcare professionals."""
    
    elif disease_type == "Parkinson's Prediction":
        prompt = """As a medical assistant, provide helpful recommendations for someone who has been diagnosed with Parkinson's disease.
        
        Please provide:
        1. Immediate steps they should take
        2. Lifestyle modifications
        3. Types of medical professionals they should consult
        4. Support resources and communities
        Important: Include a clear disclaimer that this is not medical advice and they should consult healthcare professionals."""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error getting recommendations: {str(e)}"


def load_model(filename):
    working_dir = os.path.dirname(os.path.abspath(__file__))
    return pickle.load(open(f'{working_dir}/models/{filename}', 'rb'))

diabetes_model = load_model('diabetes_model.sav')
heart_disease_model = load_model('heart_disease_model.sav')
parkinsons_model = load_model('parkinsons_model.sav')


def diabetes_ui():
    st.write("### Enter Diabetes Details")
    sex = st.selectbox('Select Sex', options=['Male', 'Female'])
    pregnancies = st.text_input('Number of Pregnancies') if sex == 'Female' else '0'
    glucose = st.text_input('Glucose Level')
    blood_pressure = st.text_input('Blood Pressure')
    skin_thickness = st.text_input('Skin Thickness')
    insulin = st.text_input('Insulin Level')
    bmi = st.text_input('BMI')
    dpf = st.text_input('Diabetes Pedigree Function')
    age = st.text_input('Age')
    inputs = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]

    if st.button('Predict Diabetes'):
        try:
            user_input = [float(x) for x in inputs]
            prediction = diabetes_model.predict([user_input])
            if prediction[0] == 1:
                st.error('Diabetic. Please consult a doctor.')
                display_recommendations('Diabetes Prediction', user_input)
            else:
                st.success('Not diabetic.')
        except ValueError:
            st.error("Invalid input. Enter numeric values.")

def heart_disease_ui():
    st.write("### Enter Heart Disease Details")
    age = st.text_input('Age')
    sex_option = st.selectbox('Sex', options=['Male', 'Female'])
    sex = '1' if sex_option == 'Male' else '0'
    cp = st.text_input('Chest Pain Type')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Cholesterol')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Max Heart Rate')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of peak exercise ST segment')
    ca = st.text_input('Major vessels colored by fluoroscopy')
    thal = st.text_input('Thal (0=normal; 1=fixed defect; 2=reversible defect)')
    inputs = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    if st.button('Predict Heart Disease'):
        try:
            user_input = [float(x) for x in inputs]
            prediction = heart_disease_model.predict([user_input])
            if prediction[0] == 1:
                st.error('Heart disease detected. Please consult a doctor.')
                display_recommendations('Heart Disease Prediction', user_input)
            else:
                st.success('No heart disease.')
        except ValueError:
            st.error("Invalid input. Enter numeric values.")

def parkinsons_ui():
    st.write("### Enter Parkinson's Details")
    inputs = [st.text_input(f"{label}") for label in [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
        'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
        'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
        'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'Spread1',
        'Spread2', 'D2', 'PPE']]
    
    if st.button("Predict Parkinson's"):
        try:
            user_input = [float(x) for x in inputs]
            prediction = parkinsons_model.predict([user_input])
            if prediction[0] == 1:
                st.error("Parkinson's disease detected. Please consult a doctor.")
                display_recommendations("Parkinson's Prediction", user_input)
            else:
                st.success("No Parkinson's disease.")
        except ValueError:
            st.error("Invalid input. Enter numeric values.")

def display_recommendations(disease_type, user_input):
    with st.spinner('Getting medical recommendations...'):
        recommendations = get_medical_assistance(disease_type, user_input)
        st.write("### Medical Assistance Recommendations:")
        st.markdown(recommendations)


st.set_page_config(page_title="Health Assistant", layout="wide")

if 'selected_disease' not in st.session_state:
    st.session_state.selected_disease = None

if st.session_state.selected_disease is None:
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Multiple Disease Prediction System</h1>", unsafe_allow_html=True)
    st.write("### Select a disease prediction model below:")
    if st.button('Diabetes Prediction'):
        st.session_state.selected_disease = 'Diabetes Prediction'
    elif st.button('Heart Disease Prediction'):
        st.session_state.selected_disease = 'Heart Disease Prediction'
    elif st.button("Parkinson's Prediction"):
        st.session_state.selected_disease = "Parkinson's Prediction"
else:
    if st.session_state.selected_disease == 'Diabetes Prediction':
        diabetes_ui()
    elif st.session_state.selected_disease == 'Heart Disease Prediction':
        heart_disease_ui()
    elif st.session_state.selected_disease == "Parkinson's Prediction":
        parkinsons_ui()

    if st.button("Back to Main Menu"):
        st.session_state.selected_disease = None
