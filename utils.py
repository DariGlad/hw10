import json

DATA_PATH = "candidates.json"


def load_candidates(path=DATA_PATH):
    """
    Получает данные всех кандидатов
    :param path: получает название файла json
    :return: список словарей кандидатов
    """
    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)
        return data


def get_candidate_by_id(pk):
    """
    возвращает кандидата по id
    :param pk: int
    :return: словарь кандидата
    """
    candidates = load_candidates()
    for candidate in candidates:
        if pk == candidate["id"]:
            return candidate


def get_candidates_by_skill(skill):
    """
    возвращает список кандидатов по умению
    :param skill: str
    :return: список словарей кандидатов
    """
    candidates = load_candidates()
    candidates_skilled = []
    for candidate in candidates:
        skills = candidate["skills"].lower().split(", ")
        if skill in skills:
            candidates_skilled.append(candidate)
    return candidates_skilled


def build_html_one_candidate(candidate):
    """
    возвращает код HTML одного кандидата
    :param candidate: dict
    :return: строку кода html
    """
    html_candidate = f"<img src=\"{candidate['picture']}\">\n"
    html_candidate += f"Имя кандидата - {candidate['name']}\n"
    html_candidate += f"Позиция кандидата - {candidate['position']}\n"
    html_candidate += f"Навыки: {candidate['skills']}"
    return f"<pre>{html_candidate}</pre>"


def build_html_more_candidates(candidates):
    """
    Возвращает код html нескольких кандидатов
    :param candidates: список словарей
    :return: строку кода html
    """
    html_candidates = ""
    for candidate in candidates:
        html_candidates += f"Имя кандидата - {candidate['name']}\n"
        html_candidates += f"Позиция кандидата - {candidate['position']}\n"
        html_candidates += f"Навыки: {candidate['skills']}\n"
    return f"<pre>{html_candidates}</pre>"


