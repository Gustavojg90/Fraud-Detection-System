import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv('transactions.csv')

df['transaction_hour'] = pd.to_datetime(df['date']).dt.hour

if 'is_fraud' not in df.columns:
    df['is_fraud'] = (df['amount'] > 1000).astype(int)  # Un ejemplo de cómo etiquetar transacciones fraudulentas

X = df[['amount', 'transaction_hour']] 
y = df['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

