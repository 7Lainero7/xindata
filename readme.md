# Freelancer Earnings NLP System

## Описание

Этот проект — прототип системы анализа данных о доходах фрилансеров с возможностью отвечать на вопросы на естественном языке с помощью LLM (Llama/Mistral).

---

## Быстрый старт

### 1. Клонируйте репозиторий

```sh
git clone https://github.com/7Lainero7/xindata.git
cd xindata
```

### 2. Установите зависимости

**Локально (Python 3.10+):**
```sh
python -m venv .venv
source .venv/bin/activate  # или .venv\Scripts\activate на Windows
pip install --upgrade pip
pip install -r requirements.txt
```

**Или через Docker:**
```sh
docker build -t freelance-llama .
docker run -it --rm -v $(pwd):/app freelance-llama
```
> **Примечание:** Если модель Llama большая, используйте volume для монтирования файла модели.

### 3. Скачайте модель Llama/Mistral

Модель будет скачана автоматически при первом запуске, если её нет в папке `models/`.  
Путь и URL модели можно изменить в `appdir/__init__.py` или `appdir/functions.py`.

### 4. Подготовьте kaggle.json

- Получите API-токен на [Kaggle](https://www.kaggle.com/settings/account) (Download API Token).
- Поместите файл `kaggle.json` в корень проекта или укажите путь в настройках.

### 5. Запуск CLI

```sh
python main.py
```
или
```sh
python main.py --query "Какой средний доход у экспертов в Европе?"
```

---

## Пример вопроса

- Насколько выше доход у фрилансеров, принимающих оплату в криптовалюте, по сравнению с другими способами оплаты?
- Как распределяется доход фрилансеров в зависимости от региона проживания?
- Какой процент фрилансеров, считающих себя экспертами, выполнил менее 100 проектов?
