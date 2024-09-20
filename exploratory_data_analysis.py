import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('transactions.csv')

df['transaction_hour'] = pd.to_datetime(df['date']).dt.hour

plt.figure(figsize=(10, 6))
sns.histplot(df['amount'], bins=50)
plt.title('Distribución de Cantidades de Transacciones')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='transaction_hour', data=df)
plt.title('Transacciones por Hora')
plt.show()

