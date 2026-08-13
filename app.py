import streamlit as st
import pandas as pd
import joblib
import base64

# Load trained model
model = joblib.load("model/student_model.pkl")

# Page configuration
st.set_page_config(
    page_title="AI Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)
# Display project GIF
with open("assets/AI_STUDENT_PERFORMANCE_CAPITAL_TYPING.gif", "rb") as file:
    gif_data = base64.b64encode(file.read()).decode()

st.markdown(
    f"""
    <div style="text-align:center; margin-bottom:20px;">
        <img src="data:image/gif;base64,{gif_data}"
             style="width:100%; max-width:1100px; border-radius:15px;">
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🎓 AI Student Performance Predictor")
st.write("Predict a student's expected final marks using Machine Learning.")

st.divider()

# Student inputs
st.subheader("Enter Student Details")

attendance = st.slider(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

study_hours = st.slider(
    "Daily Study Hours",
    min_value=0,
    max_value=12,
    value=5
)

previous_marks = st.slider(
    "Previous Examination Marks",
    min_value=0,
    max_value=100,
    value=60
)

assignment_marks = st.slider(
    "Assignment Marks",
    min_value=0,
    max_value=100,
    value=70
)

internal_marks = st.slider(
    "Internal Assessment Marks",
    min_value=0,
    max_value=100,
    value=65
)

# Prediction
if st.button("🚀 Predict Final Marks", use_container_width=True):

    input_data = pd.DataFrame([{
        "Attendance": attendance,
        "Study_Hours": study_hours,
        "Previous_Marks": previous_marks,
        "Assignment_Marks": assignment_marks,
        "Internal_Marks": internal_marks
    }])

    prediction = model.predict(input_data)[0]

    prediction = max(0, min(100, prediction))

    if prediction >= 85:
        performance = "Excellent 🌟"
    elif prediction >= 70:
        performance = "Good 👍"
    elif prediction >= 50:
        performance = "Average 📚"
    else:
        performance = "Needs Improvement 💪"

    st.success(f"Predicted Final Marks: {prediction:.2f}/100")

    st.info(f"Performance Level: **{performance}**")

    st.divider()

    st.subheader("📊 Student Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Attendance", f"{attendance}%")
        st.metric("Study Hours", f"{study_hours} hrs/day")
        st.metric("Previous Marks", f"{previous_marks}")

    with col2:
        st.metric("Assignment Marks", f"{assignment_marks}")
        st.metric("Internal Marks", f"{internal_marks}")
        st.metric("Predicted Marks", f"{prediction:.2f}")