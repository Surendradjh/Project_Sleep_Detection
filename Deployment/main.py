import streamlit as st

# Set page config
st.set_page_config(page_title="Sleep Detection System", layout="centered")

# Add background image using custom CSS
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1527689368864-3a821dbccc34");  /* Replace with your preferred background URL */
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}

.stApp {
background-color: rgba(255, 255, 255, 0.8);  /* Semi-transparent white background */
padding: 2rem;
# border-radius: 20px;
# max-width: 900px;
# margin: auto;
}

h1 {
color: #2c3e50;
text-align: center;
}

h3 {
color: #34495e;
}

p {
color: #2d3436;
font-size: 1.1rem;
line-height: 1.6;
}
</style>
'''

# Inject CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title and subheaders
st.title("😴 Sleep Detection System")
st.subheader("🔍 Business Problem")

# Business problem description
st.markdown("""
<p>In recent years, mental health challenges have been on the rise, especially among working professionals. One key factor contributing to this issue is abnormal or poor sleep patterns.</p>

<p>To help address this, we propose developing a <strong>sleep detection system</strong> that monitors and analyzes how individuals sleep. This system uses movement-based data—specifically <strong>ENMO</strong> (Euclidean Norm Minus One) and <strong>Angle-Z</strong)—collected through wearable devices. These metrics allow us to determine sleep state and provide insights into sleep quality and behavior.</p>

<p><strong>Why it matters:</strong></p>
<ul>
    <li>Lack of sleep or irregular patterns can lead to stress, burnout, and reduced productivity.</li>
    <li>Oversleeping can indicate inactivity, lethargy, or deeper health issues.</li>
</ul>

<p><strong>Our system aims to provide:</strong></p>
<ul>
    <li>⏰ Warnings for insufficient or irregular sleep.</li>
    <li>📉 Alerts when oversleeping patterns emerge.</li>
    <li>✅ Positive reinforcement for healthy and consistent sleep routines.</li>
</ul>

<p>With real-time insights and personalized feedback, this system supports better sleep hygiene and overall mental and physical well-being.</p>
""", unsafe_allow_html=True)
