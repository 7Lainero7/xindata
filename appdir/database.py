import sqlite3
import pandas as pd


def csv_to_sqlite(csv_path: str, db_path: str = 'freelancers.db', table_name: str = 'freelancers'):
    """
    Загружает данные из CSV-файла в таблицу SQLite.

    :param csv_path: str, путь к CSV-файлу
    :param db_path: str, путь к базе данных SQLite (по умолчанию 'freelancers.db')
    :param table_name: str, имя таблицы для сохранения данных (по умолчанию 'freelancers')
    """
    # Читаем CSV-файл в DataFrame
    df = pd.read_csv(csv_path)
    # Открываем соединение с базой данных SQLite
    conn = sqlite3.connect(db_path)
    # Сохраняем DataFrame в таблицу базы данных
    df.to_sql(table_name, conn, index=False, if_exists='replace')
    # Закрываем соединение
    conn.close()
