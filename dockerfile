FROM python:3.11

# Установим необходимые системные зависимости
RUN apt-get update && \
    apt-get install -y cmake build-essential && \
    rm -rf /var/lib/apt/lists/*

# Копируем файлы проекта
WORKDIR /app
COPY . /app

# Установим зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# (Опционально) Установим llama-cpp-python
RUN pip install llama-cpp-python

CMD ["python", "main.py"]