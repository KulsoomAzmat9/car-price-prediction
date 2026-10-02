🚗 Car Price Prediction - AI Project

Predict used car selling price using Machine Learning.

🤖 Algorithm Used
* Model: Random Forest Regressor*
- Why: Best accuracy (85-90%) for this dataset, handles both numerical and categorical data, avoids overfitting.

*Techniques Used:*
1. One-Hot Encoding - to convert Fuel_Type, Seller_Type, Transmission to numbers
2. train_test_split (80% train, 20% test) - for model evaluation
3. Pickle - to save model as model.pkl and columns as columns.pkl

Pipeline:
1. Load car_data.csv
2. One-Hot Encoding for categorical columns
3. Train Random Forest
4. Save as model.pkl

✨ Live App
Modern purple gradient UI with big result display (36px).

📁 Project Structure
car-price-prediction/
├── http://app.py - Main Streamlit app
├── http://train.py - Model training code
├── car_data.csv - Dataset
├── http://model.pkl & http://columns.pkl - Trained model
├── http://requirements.txt - Dependencies
├── http://app-output.png - App screenshot
└── http://powershell-proof.png - Terminal proof

▶️ How to Run (From PowerShell)
```bash
E:
cd car-price-prediction
py -m pip install -r requirements.txt
py -m streamlit run app.py
Open: http://localhost:8501

🎯 Input Features
Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner

📸 Output
> 💰 Estimated: 4.97 lakhs

Made with Python + Streamlit + Scikit-Learn