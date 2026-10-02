import pandas as pd, numpy as np
np.random.seed(42)
n=500
years=np.random.randint(2005,2023,n)
present_price=np.round(np.random.uniform(1.5,35.0,n),2)
kms=np.random.randint(5000,150000,n)
fuel=np.random.choice(['Petrol','Diesel','CNG'],n,p=[0.55,0.35,0.10])
seller=np.random.choice(['Dealer','Individual'],n,p=[0.6,0.4])
trans=np.random.choice(['Manual','Automatic'],n,p=[0.7,0.3])
owner=np.random.choice([0,1,2,3],n,p=[0.5,0.35,0.1,0.05])
age=2024-years
selling=present_price*(1-age*0.05)-(kms/100000)*0.5-owner*0.4
selling=selling+np.where(fuel=='Diesel',0.5,0)+np.where(trans=='Automatic',0.7,0)+np.random.normal(0,0.6,n)
selling=np.clip(selling,0.5,35)
df=pd.DataFrame({
'Year':years,'Present_Price':present_price,'Kms_Driven':kms,
'Fuel_Type':fuel,'Seller_Type':seller,'Transmission':trans,
'Owner':owner,'Selling_Price':np.round(selling,2)
})
df.to_csv('car_data.csv', index=False)
print(f"Done! Created car_data.csv with {len(df)} rows - Size: {df.memory_usage(deep=True).sum()/1024:.1f} KB")