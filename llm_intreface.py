import re

from llama_cpp import Llama

from appdir import data_description
from appdir.functions import ensure_llama_model


model_path = ensure_llama_model()
llm = Llama(model_path=model_path,
            n_ctx=2048,  # Максимальный контекст (ввод + вывод)
            n_threads=8  # Количество потоков CPU
        )


def llm_generate_sql(question: str) -> str:
    prompt = f"""
    Всегда пиши полный SQL-запрос одной строкой, обязательно указывай FROM freelancers и GROUP BY, если требуется. Всегда заканчивай запрос точкой с запятой.
    # Таблица: freelancers
    # Поля: Job_Category, Platform, Experience_Level, Client_Region, Payment_Method, Earnings_USD, Job_Completed

    # Примеры:
    В: Какой средний доход у фрилансеров из Австралии?
    SQL: SELECT AVG(Earnings_USD) FROM freelancers WHERE Client_Region = 'Australia';

    В: Сколько проектов в среднем выполняют специалисты уровня Intermediate на платформе Upwork?
    SQL: SELECT AVG(Job_Completed) FROM freelancers WHERE Experience_Level = 'Intermediate' AND Platform = 'Upwork';

    В: Как распределяется средний доход по платформам?
    SQL: SELECT Platform, AVG(Earnings_USD) FROM freelancers GROUP BY Platform;

    В: Какой способ оплаты самый популярный среди фрилансеров из Канады?
    SQL: SELECT Payment_Method, COUNT(*) FROM freelancers WHERE Client_Region = 'Canada' GROUP BY Payment_Method ORDER BY COUNT(*) DESC;

    Вопрос: {question}
    SQL:
    """
    response = llm.create_chat_completion(max_tokens=512,
                                          messages=[{"role": "user", "content": prompt}])
    content = response['choices'][0]['message']['content']

    # Оставляем только первую строку, начинающуюся с SELECT
    for line in content.splitlines():
        if line.strip().upper().startswith("SELECT"):
            return line.strip()
    # Если не найдено, ищем через регулярку
    match = re.search(r"(SELECT[\s\S]+?;)", content, re.IGNORECASE)
    if match:
        return match.group(1)
    # Если не найдено, возвращаем пустую строку или логируем ошибку
    return ""
