import os
import json
import zipfile
import requests

import pandas as pd
from tqdm import tqdm
from kaggle.api.kaggle_api_extended import KaggleApi

from appdir import MODEL_NAME, MODEL_DIR, MODEL_URL


def download_kaggle_csv(dataset: str, file_name: str, download_path: str, kaggle_json_path: str = "kaggle.json"):
    """
    Скачивает .csv файл с Kaggle.

    :param dataset: str, например 'shohinurpervezshohan/freelancer-earnings-and-job-trends'
    :param file_name: str, например 'freelancer_earnings_bd.csv'
    :param download_path: str, путь для сохранения файла
    :param kaggle_json_path: str, путь к файлу kaggle.json с токеном
    """
    # Установить переменные окружения для kaggle API
    os.makedirs(os.path.dirname(download_path), exist_ok=True)
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


def download_file(url: str, save_path: str):
    """Скачивает файл с прогресс-баром."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    response = requests.get(url, headers=headers, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))
    progress = tqdm(
        total=total_size,
        unit='B',
        unit_scale=True,
        desc=f"Скачивание {os.path.basename(save_path)}"
    )
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                progress.update(len(chunk))
    progress.close()


def ensure_llama_model():
    """Проверяет наличие модели и скачивает при необходимости."""
    model_path = os.path.join(MODEL_DIR, MODEL_NAME)
    if not os.path.exists(model_path):
        print("🛠️ Начинаем загрузку модели...")
        try:
            download_file(MODEL_URL, model_path)
            print(f"✅ Модель успешно сохранена в: {model_path}")
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            print("Проверьте подключение к интернету или URL модели.")
    else:
        print(f"Модель уже существует: {model_path}")
    return model_path
