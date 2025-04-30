import streamlit as st
import numpy as np
import joblib

# Load model and scaler
scaler = joblib.load("Scaler.pkl")
model = joblib.load("model.pkl")

# App title
st.set_page_config(page_title="Real Estate Price Predictor", page_icon="🏠")
st.title("🏠 Real Estate Price Prediction App (USA)")
st.write("Use this app to predict property prices based on features.")

st.sidebar.header("📊 About the App")
st.sidebar.info("""
This app uses a machine learning model trained on USA real estate data.  
Input the number of bedrooms, bathrooms, and square footage to predict the price.
""")

# Add a form for cleaner UI
with st.form("prediction_form"):
    st.subheader("🧾 Enter Property Details")
    
    bed = st.slider("Number of Bedrooms", min_value=1, max_value=40, value=2)
    bath = st.slider("Number of Bathrooms", min_value=1, max_value=20, value=1)
    size = st.slider("Size (in square feet)", min_value=300, max_value=10000, value=1000, step=50)

    submitted = st.form_submit_button("Predict Price")

st.divider()

if submitted:
    st.balloons()
    
    # Prepare input and scale
    X = np.array([bed, bath, size])
    X_scaled = scaler.transform([X])
    
    # Predict
    prediction = model.predict(X_scaled)[0]
    prediction = max(prediction, 5000 if sum(X) > 0 else 0)

    # Display result
    st.metric(label="💰 Estimated Price (USD)", value=f"${prediction:,.2f}")

    st.success("Prediction completed successfully!")

else:
    st.info("👆 Fill the form and click **Predict Price**")

# Optional footer
st.divider()
st.caption("📌 Note: This prediction is based on a machine learning model and should not be used for financial decisions.")
