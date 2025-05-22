from llama_cpp import Llama

from appdir import data_description
from appdir.functions import ensure_llama_model


model_path = ensure_llama_model()
llm = Llama(model_path=model_path)


def llm_generate_sql(question: str) -> str:
    """
    Генерирует SQL-запрос на основе заданного вопроса на естественном
    языке с помощью LLM.
    :param question: str, вопрос на естественном языке, который
    требуется преобразовать в SQL-запрос.
    :return: str, сгенерированный SQL-запрос.
    """
    prompt = (
        f"Вот описание структуры данных:\n{data_description}\n"
        f"Переведи вопрос в SQL: '{question}'"
    )
    response = llm.create_chat_completion(messages=[{"role": "user", "content": prompt}])
    return response['choices'][0]['message']['content']
