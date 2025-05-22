from llama_cpp import Llama


llm = Llama(model_path="mistral-7b-instruct-v0.1.Q4_K_M.gguf")


def llm_generate_sql(question: str) -> str:
    """
    Генерирует SQL-запрос на основе заданного вопроса на естественном языке с помощью LLM.

    :param question: str, вопрос на естественном языке, который требуется преобразовать в SQL-запрос.
    :return: str, сгенерированный SQL-запрос.
    """
    prompt = f"Переведи вопрос в SQL: '{question}'"
    response = llm.create_chat_completion(messages=[{"role": "user", "content": prompt}])
    return response['choices'][0]['message']['content']