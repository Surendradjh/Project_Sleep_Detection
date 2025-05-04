import streamlit as st 

import pandas as pd 



# Set page config

st.set_page_config(page_title="Sleep Detection Project", layout="wide")



# Custom styling

st.markdown(

    """

    <style>

        .main {

            background-color: #f2f6fa;

        }

        .title {

            color: #003366;

            font-size: 42px;

            font-weight: bold;

        }

        .subtitle {

            color: #005599;

            font-size: 26px;

            margin-bottom: 10px;

        }

        .section-text {

            color: #333333;

            font-size: 16px;

            line-height: 1.6;

        }

        .data-title {

            font-size: 20px;

            color: #004080;

            font-weight: 600;

        }

    </style>

    """, unsafe_allow_html=True

)



# Title

st.markdown('<div class="title">🛌 Sleep Detection Project</div>', unsafe_allow_html=True)



# Subheader

st.markdown('<div class="subtitle">📘 Readme & Dataset Overview</div>', unsafe_allow_html=True)



# Dataset Explanation Section

with st.expander("📈 Train Series Data - Raw Accelerometer Readings"):

    st.markdown("""

    <div class="section-text">

    This dataset contains accelerometer readings collected every 5 seconds. <br><br>

    <b>Columns:</b><br>

    • <b>series_id</b> – Unique identifier for each recording session.<br>

    • <b>step</b> – Time step (every 5 seconds).<br>

    • <b>timestamp</b> – Actual datetime of the reading.<br>

    • <b>anglez</b> – Arm orientation (from accelerometer axes).<br>

    • <b>enmo</b> – Euclidean Norm Minus One; lower values indicate inactivity (possible sleep).<br>

    </div>

    """, unsafe_allow_html=True)

    

    raw_data = pd.read_csv("sample_raw_data.csv")

    st.markdown('<div class="data-title">📊 Sample Raw Data</div>', unsafe_allow_html=True)

    st.dataframe(raw_data, use_container_width=True)



with st.expander("🌙 Train Events Data - Sleep Events"):

    st.markdown("""

    <div class="section-text">

    This dataset contains labeled sleep events like onset and wakeup.<br><br>

    <b>Columns:</b><br>

    • <b>series_id</b> – Identifier for each device.<br>

    • <b>night</b> – Night number (to track sleep per day).<br>

    • <b>event</b> – 'onset' (start of sleep) or 'wakeup' (end of sleep).<br>

    • <b>step</b> – Time step when event occurred.<br>

    • <b>timestamp</b> – Datetime of the event.<br>

    </div>

    """, unsafe_allow_html=True)

    

    event_data = pd.read_csv("train_events.csv")

    st.markdown('<div class="data-title">📊 Sleep Events Data</div>', unsafe_allow_html=True)

    st.dataframe(event_data, use_container_width=True)



# Sleep Rules Section

with st.expander("ℹ Sleep Detection Logic & Rules"):

    st.markdown("""

    <div class="section-text">

    <b>✅ 1. Minimum Sleep Duration:</b> A sleep period must be ≥ 30 minutes.<br><br>



    <b>✅ 2. Short Activity Interruptions:</b> Interruptions ≤ 30 mins are still within the same sleep window.<br><br>



    <b>✅ 3. Device Must Be Worn:</b> If not worn, sleep detection is not possible.<br><br>



    <b>✅ 4. Longest Sleep Period Counts:</b> Only the longest detected sleep session per night is recorded.<br><br>



    <b>✅ 5. No Events Without Valid Sleep:</b> No data means no onset/wakeup is recorded.<br><br>



    <b>✅ 6. Sleep Doesn’t Need to Cross Midnight:</b> Sleep can occur anytime within the day.<br><br>



    <b>✅ 7. Number of Nights ≈ Recording Duration:</b> Expect one sleep window per day of device use.<br>

    </div>

    """, unsafe_allow_html=True)



# Footer
st.markdown("---")
st.markdown("<center><sub>Developed By Surendra | Sleep Insights</sub></center>", unsafe_allow_html=True)    