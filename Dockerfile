FROM python:3.14

WORKDIR /credit-card-ml-deployment

#Копирование зависимостей
COPY requirements.txt ./

#Копирование кода и модели

COPY app/ ./app
COPY models/ ./models
RUN pip install --no-cache-dir -r requirements.txt
#Открытие порта
EXPOSE 5000

#Запуск приложения
CMD [ "python","app/api.py" ]