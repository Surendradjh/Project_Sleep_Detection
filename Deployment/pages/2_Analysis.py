import streamlit as st



# Set page config
st.set_page_config(
    page_title="Sleep Data Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title
st.markdown("<h1 style='color:#1f77b4;'>🛌 Sleep Data Analysis Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar - Navigation
st.sidebar.header("📊 Select Analysis Type")
analysis_type = st.sidebar.selectbox(
    "Choose analysis type:",
    ["Raw data analysis", "Events data analysis", "Combined data analysis"]
)

image_width = None  # fixed width for all images

# Raw Data Analysis
if analysis_type == "Raw data analysis":
    st.markdown("### 📌 Year-wise Participants Overview")
    st.image("plots/Year-wise Participants.png", width=image_width)
    st.info("""
    Majority of the data was collected in 2018, with a drop at both ends of the timeline. 
    This suggests participant attrition or data collection starting/ending phases.
    """)

    st.markdown("### 📌 ENMO Statistics")
    st.image("plots/enmo_stats.png", width=image_width)
    st.success("""
    - ENMO measures movement intensity.
    - Observed values range from 0 to 11.43.
    """)

    st.markdown("### 📌 ENMO Distribution")
    st.image("plots/enmo distribution.png", width=image_width)
    st.warning("""
    - Highly right-skewed, resembling a log-normal pattern.
    - Indicates frequent inactivity (sleep) periods.
    - 0.70+ values appear consistently—reflects light/moderate activity.
    """)

    st.markdown("### 📌 ENMO Pattern by Time")
    st.image("plots/hour vs enmo.png", width=image_width)
    st.info("""
    - Dip in ENMO around hour 10 suggests rest.
    - Spike at hour 18 indicates peak activity time.
    """)

    st.markdown("### 📌 Anglez Data Distribution")
    st.image("plots/anglez_distribution.png", width=image_width)
    st.success("""
    - Mostly bell-shaped, slightly right-skewed.
    - Angle 0 most frequent → resting hand positions.
    - Range -84 to -89 reflects hand movement.
    """)

    st.markdown("### 📌 Step Count Extremes")
    st.image("plots/Top & bottom steps vs participents.png", width=image_width)
    st.warning("""
    - Top: Long usage → more active individuals (up to 1.4M steps).
    - Bottom: Shorter durations → lower step count users.
    """)

# Events Data Analysis
elif analysis_type == "Events data analysis":
    st.markdown("### 📌 Participants Overview")
    st.image("plots/events_data.png", width=image_width)
    st.info("Collected data from *277 individuals* via raw accumulators.")

    st.markdown("### 📌 Fault Data")
    st.image("plots/fault_data.png", width=image_width)
    st.warning("Total *5 fault records* found in event data.")

    st.markdown("### 📌 Individuals vs Nights")
    st.image("plots/individuals vs nights.png", width=image_width)
    st.success("""
    - ID *78569a801a38* has maximum nights.
    - Right-skewed: few have long-term data; many have short records.
    """)

    st.markdown("### 📌 Individual Sleep Patterns")
    st.image("plots/sleep_pattern.png", width=image_width)
    st.info("""
    - Sleep patterns help assess routine quality.
    - Oversleeping and undersleeping both raise health concerns.
    """)

# Combined Analysis
elif analysis_type == "Combined data analysis":
    st.markdown("### 📌 Feature Correlation (Anglez vs ENMO)")
    st.image("plots/correlation between anglez vs enmo.png", width=image_width)
    st.warning("""
    - Slight negative relationship.
    - Alone, they don’t clearly classify sleep/wake states.
    """)

    st.markdown("### 📌 ENMO vs Anglez Events")
    st.image("plots/enmo_vs_anlgez.png", width=image_width)
    st.success("""
    - No strong linear correlation.
    - ENMO is active even during sleep onset.
    - Combine features + sequence modeling might help.
    """)

    st.markdown("### 📌 Feature Transformation Insight")
    st.image("plots/feature_transformation.png", width=image_width)
    st.warning("""
    - Data remains non-linear after transformation.
    - Models relying on normality (e.g., SVM, NB) may underperform.
    - Even KNN may fail due to skewed patterns.
    """)

# Footer
st.markdown("---")
st.markdown("<center><sub>Developed By Surendra | Sleep Insights</sub></center>", unsafe_allow_html=True)    