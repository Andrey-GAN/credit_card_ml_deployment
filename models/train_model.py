import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

data_frame=pd.read_csv(f"data/UCI_Credit_Card.csv")

# Организуем пайлайн для модели
df_without_target=data_frame.drop(columns=['default.payment.next.month','ID'])
df_without_target=df_without_target.reindex(sorted(df_without_target.columns),axis=1)
X=df_without_target.values
y=data_frame['default.payment.next.month']

model=LogisticRegression(max_iter=100000)
try:
    model.fit(X, y)
    print("Модель обучена")
    with open('modelv1.pkl', 'wb') as output:
        pickle.dump(model, output)
    print("Файл modelv1.pkl создан")
except Exception as e:
    print("Ошибка:", e)