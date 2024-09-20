import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('transactions.csv')

df['transaction_hour'] = pd.to_datetime(df['date']).dt.hour

if 'is_fraud' not in df.columns:
    df['is_fraud'] = (df['amount'] > 1000).astype(int)

X = df[['amount', 'transaction_hour']]
y = df['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

for index, row in X_test.iterrows():
    transaction = row.values.reshape(1, -1)
    prediction = model.predict(transaction)  
    print(f"Transacción {index + 1}: {'Fraudulenta' if prediction[0] == 1 else 'No Fraudulenta'}")


