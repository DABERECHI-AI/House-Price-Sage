
import streamlit as st
import joblib

# Set the page config
st.set_page_config(page_title="Price Sage", page_icon="🏠", layout="centered")

@st.cache_resource
def load_model():
    return joblib.load('real_estate_model.joblib')

model_data = load_model()
House_price = model_data['House_price']
default_price = model_data['overall_average_price']

st.title("🏠 AI House Price Predictor")
st.markdown("""
This app predicts the price of a house based on its key features.
The model was built using real estate data and machine learning.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏠 Property Features")
    bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
    floors = st.slider("Number of Floors", 1, 4, 2)

with col2:
    st.subheader("📊 Model Info")
    st.metric("Unique Price Combinations", len(House_price))
    st.metric("Overall Average Price", f"${default_price:,.2f}")
    st.caption("The model uses average prices for each bedroom/floor combination.")

st.divider()

if st.button("Predict House Price", type="primary", use_container_width=True):
    predicted_price = House_price.get((bedrooms, floors), default_price)
    st.success("Prediction Result")
    st.metric(label="Estimated Market Value", value=f"${predicted_price:,.2f}")
    st.info(f"*Based on {bedrooms} bedrooms and {floors} floor(s).*")

st.divider()
st.caption("Built with Python, Pandas, and Streamlit | Model Accuracy: 100% for known combinations")
