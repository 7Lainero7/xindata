import os
import json

import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi


def download_kaggle_csv(dataset: str, file_name: str, download_path: str, kaggle_json_path: str = "kaggle.json"):
    """
    Скачивает .csv файл с Kaggle.

    :param dataset: str, например 'shohinurpervezshohan/freelancer-earnings-and-job-trends'
    :param file_name: str, например 'freelancer_earnings_bd.csv'
    :param download_path: str, путь для сохранения файла
    :param kaggle_json_path: str, путь к файлу kaggle.json с токеном
    """
    # Установить переменные окружения для kaggle API
    with open(kaggle_json_path, "r") as f:
        creds = json.load(f)
    os.environ["KAGGLE_USERNAME"] = creds["username"]
    os.environ["KAGGLE_KEY"] = creds["key"]

    api = KaggleApi()
    api.authenticate()
    os.makedirs(download_path, exist_ok=True)
    api.dataset_download_file(dataset, file_name, path=download_path, force=True)
    # Распаковываем, если скачан архив
    zip_path = os.path.join(download_path, file_name + '.zip')
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(download_path)
        os.remove(zip_path)


def drop_freelancer_id(csv_path: str, output_path: str = None):
    """
    Удаляет столбец 'Freelancer_ID' из csv-файла.

    :param csv_path: путь к исходному csv-файлу
    :param output_path: путь для сохранения результата (если None — перезаписывает исходный файл)
    """
    df = pd.read_csv(csv_path)
    if 'Freelancer_ID' in df.columns:
        df = df.drop(columns=['Freelancer_ID'])
    if output_path is None:
        output_path = csv_path
    df.to_csv(output_path, index=False)
