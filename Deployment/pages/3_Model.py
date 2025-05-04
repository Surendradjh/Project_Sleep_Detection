import streamlit as st
import pickle
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from  datetime import datetime as dt
import time

t1 = dt.now().strftime("%Y-%m-%d %H:%M:%S")


st.set_page_config(
    page_title="🛌 Sleep Pattern Detection",
    layout="wide",
    initial_sidebar_state="expanded"
)



with open("pipe.pkl", 'rb') as file:
    model = pickle.load(file)

# App Title
st.markdown("<h1 style='color:#1f77b4;'>🧠 Sleep Pattern Prediction App</h1>", unsafe_allow_html=True)
st.markdown("---")

# Input Section
st.markdown("### 🔍 Enter Sensor Values")



col1, col2 = st.columns(2)
with col1:
    enmo = st.number_input("ENMO value", min_value=0.0, format="%.4f", help="Measures movement intensity")
with col2:
    anglez = st.number_input("Anglez value", min_value=-90.0, max_value=90.0, format="%.2f", help="Represents wrist angle")


st.markdown("### 🎯 Prediction Result")
if st.button("🧪 Predict Sleep State"):
    input_data = {"enmo": enmo, "anglez": anglez}
    df = pd.DataFrame([input_data])
    
    try:
        prediction = model.predict(df)
        if prediction[0] == 0:
            prediction="onset-Sleeping"
        else:
            prediction = "Wakeup"
        st.success(f"✅ Predicted Sleep State: *{prediction}*")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

st.markdown("---")
st.markdown("### 📊 Random Individual's Sleep Pattern")

try:
    sleep_patterns = pd.read_csv("Sleep_patterns.csv")
    s_id = st.selectbox("Select user:",np.array(sleep_patterns['series_id'].unique()))
    b = sleep_patterns.loc[sleep_patterns['series_id'] == s_id, ["night", 'sleep_hours']]
    nights=list(range(1,len(b['night'])+1))
    b['night']=nights
    st.markdown(f"##### 🧬 Sleep Data for ID: {s_id}")

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=b['night'], y=b['sleep_hours'], palette="Blues", ax=ax)
    ax.set_xlabel("Night")
    ax.set_ylabel("Sleep Hours")
    ax.set_title("Sleep Hours per Night")
    st.pyplot(fig)

except Exception as e:
    st.error(f"⚠ Failed to load or plot sleep pattern: {e}")

st.markdown("---")
st.markdown("<center><sub>Developed By Surendra | Sleep Insights</sub></center>", unsafe_allow_html=True)    