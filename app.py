import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
header, [data-testid="stHeader"] { display: none; }
.block-container { padding-top: 20px!important; }
h1 { color: white!important; text-align: center; }
div[data-testid="stNumberInput"], div[data-testid="stSelectbox"] {
    background: white; border-radius: 10px; padding: 5px 10px;
}
.stButton>button {
    background: linear-gradient(90deg, #FF416C, #FF4B2B);
    color: white; border-radius: 25px; height: 55px;
    font-size: 20px; font-weight: bold; width: 100%;
    border: none;
}
.result-big {
    background: white;
    border-radius: 15px;
    padding: 25px;
    text-align: center;
    font-size: 36px!important;
    font-weight: 900;
    color: #0d8a3e;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    animation: pop 0.5s ease;
}
@keyframes pop { 0%{transform:scale(0.8)} 100%{transform:scale(1)} }
label { color: white!important; font-weight: bold!important; }
</style>
""", unsafe_allow_html=True)

model = pickle.load(open('model.pkl','rb'))
cols = pickle.load(open('columns.pkl','rb'))

st.title("🚗 Car Price Prediction")

Year = st.number_input("Year", 2000, 2025, 2023)
Present_Price = st.number_input("Present Price (in lakhs)", 1.0, 50.0, 5.0)
Kms_Driven = st.number_input("Kms Driven", 1000, 500000, 50000)
Fuel_Type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
Seller_Type = st.selectbox("Seller Type", ["Dealer", "Individual"])
Transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
Owner = st.selectbox("Owner", [0,1,2,3])

if st.button("✨ Predict Selling Price"):
    df = pd.DataFrame([{
        'Year': Year, 'Present_Price': Present_Price,
        'Kms_Driven': Kms_Driven, 'Fuel_Type': Fuel_Type,
        'Seller_Type': Seller_Type, 'Transmission': Transmission,
        'Owner': Owner
    }])
    df = pd.get_dummies(df)
    for c in cols:
        if c not in df.columns: df[c] = 0
    df = df[cols]
    price = model.predict(df)[0]
    st.balloons()
    st.markdown(f'<div class="result-big">💰 Estimated: {price:.2f} lakhs</div>', unsafe_allow_html=True)