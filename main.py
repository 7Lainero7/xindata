import click

from llm_intreface import llm_generate_sql
from appdir.functions import download_kaggle_csv, drop_freelancer_id, ensure_llama_model
from appdir.database import csv_to_sqlite, execute_sql


@click.command()
@click.option('--query', prompt='Введите ваш вопрос', help='Вопрос для анализа')
def analyze(query):
    """
    Анализирует введённый пользователем вопрос, генерирует соответствующий SQL-запрос
    с помощью LLM, выполняет его и выводит результат.

    :param query: str, вопрос на естественном языке, который требуется преобразовать
    в SQL-запрос и выполнить.
    :return: None, результат выполнения SQL-запроса выводится в консоль.
    """
    sql_query = llm_generate_sql(query)
    print(f"SQL-запрос: {sql_query}")
    result = execute_sql(sql_query)
    print("Результат запроса:")
    for row in result:
        print(row)


if __name__ == '__main__':
    download_kaggle_csv('shohinurpervezshohan/freelancer-earnings-and-job-trends',
                         'freelancer_earnings_bd.csv', './data')
    drop_freelancer_id('data/freelancer_earnings_bd.csv')
    csv_to_sqlite('data/freelancer_earnings_bd.csv')
    analyze()
