import click

from llm_intreface import llm_generate_sql
from appdir.functions import download_kaggle_csv, drop_freelancer_id
from appdir.database import csv_to_sqlite, execute_sql


download_kaggle_csv('shohinurpervezshohan/freelancer-earnings-and-job-trends',
                        'freelancer_earnings_bd.csv',
                        './data')
drop_freelancer_id('data/freelancer_earnings_bd.csv')
csv_to_sqlite('data/freelancer_earnings_bd.csv')


@click.command()
def analyze():
    """
    Анализирует введённый пользователем вопрос, генерирует соответствующий SQL-запрос
    с помощью LLM, выполняет его и выводит результат.
    """
    print("Введите ваш вопрос (или 'exit' для выхода):")
    while True:
        query = click.prompt("> ", type=str)
        if query.lower() in ("exit", "quit"):
            break
        sql_query = llm_generate_sql(query)
        print(f"SQL-запрос: {sql_query}")
        result = execute_sql(sql_query)
        if not result or isinstance(result, str):
            print("Нет данных или произошла ошибка при выполнении запроса.")
            if isinstance(result, str):
                print(result)
        else:
            for row in result:
                print(row)


if __name__ == '__main__':
    analyze()
