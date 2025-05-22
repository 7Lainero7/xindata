import os
import json


with open("kaggle.json", "r") as f:
    creds = json.load(f)
os.environ["KAGGLE_USERNAME"] = creds["username"]
os.environ["KAGGLE_KEY"] = creds["key"]

data_description = """
Датасет содержит информацию о доходах и характеристиках фрилансеров. Ключевые поля:
- Job_Category: категория работы (например, Web Development, App Development и др.)
- Platform: платформа (например, Upwork, Fiverr и др.)
- Experience_Level: уровень опыта (Beginner, Intermediate, Expert)
- Client_Region: регион клиента (например, Asia, Europe, USA и др.)
- Payment_Method: способ оплаты (например, Crypto, PayPal, Bank Transfer, Mobile Banking)
- Job_Completed: количество завершённых проектов
- Earnings_USD: доход в долларах США
- Hourly_Rate: почасовая ставка
- Job_Success_Rate: процент успешных проектов
- Client_Rating: рейтинг клиента
- Job_Duration_Days: длительность проекта (в днях)
- Project_Type: тип проекта (Fixed, Hourly)
- Rehire_Rate: процент повторных заказов
- Marketing_Spend: расходы на маркетинг
"""