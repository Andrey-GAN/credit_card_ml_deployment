import requests

# Проверка здоровья сервера
health = requests.get('http://localhost:5000/health')
print(f"Health check: {health.json()}")

# Пример с корректными данными (все 23 признака)
test_data = {
    'LIMIT_BAL': 0, 'SEX': 2, 'EDUCATION': 0, 'MARRIAGE': 2, 'AGE': 80,
    'PAY_0': 0, 'PAY_2': 0, 'PAY_3': 0, 'PAY_4': 0, 'PAY_5': 0, 'PAY_6': 0,
    'BILL_AMT1': 5000, 'BILL_AMT2': 4000, 'BILL_AMT3': 3000, 'BILL_AMT4': 2000, 'BILL_AMT5': 1000, 'BILL_AMT6': 500,
    'PAY_AMT1': 0, 'PAY_AMT2': 0, 'PAY_AMT3': 500, 'PAY_AMT4': 0, 'PAY_AMT5': 500, 'PAY_AMT6': 500
}

test_data_extreme = {
    'LIMIT_BAL': 1000000,   # Огромный лимит
    'SEX': 1,
    'EDUCATION': 1,
    'MARRIAGE': 1,
    'AGE': 60,
    'PAY_0': 0, 'PAY_2': 0, 'PAY_3': 0, 'PAY_4': 0, 'PAY_5': 0, 'PAY_6': 0,
    'BILL_AMT1': 50000, 'BILL_AMT2': 40000, 'BILL_AMT3': 30000,
    'BILL_AMT4': 20000, 'BILL_AMT5': 10000, 'BILL_AMT6': 5000,
    'PAY_AMT1': 10000, 'PAY_AMT2': 10000, 'PAY_AMT3': 10000,
    'PAY_AMT4': 10000, 'PAY_AMT5': 10000, 'PAY_AMT6': 10000
}   


response = requests.post('http://localhost:5000/predict', json=test_data)
print(f"\nResponse: {response.json()}")

response = requests.post('http://localhost:5000/predict', json=test_data_extreme)
print(f"\nResponse: {response.json()}")

data_v1 = {
    'LIMIT_BAL': 20000, 'SEX': 1, 'EDUCATION': 2, 'MARRIAGE': 1, 'AGE': 30,
    'PAY_0': -1, 'PAY_2': 2, 'PAY_3': 0, 'PAY_4': 0, 'PAY_5': 0, 'PAY_6': 0,
    'BILL_AMT1': 5000, 'BILL_AMT2': 4000, 'BILL_AMT3': 3000, 'BILL_AMT4': 2000,
    'BILL_AMT5': 1000, 'BILL_AMT6': 500, 'PAY_AMT1': 500, 'PAY_AMT2': 500,
    'PAY_AMT3': 500, 'PAY_AMT4': 500, 'PAY_AMT5': 500, 'PAY_AMT6': 500
}

response = requests.post('http://localhost:5000/predict', json=data_v1)
print(f"\nResponse: {response.json()}")