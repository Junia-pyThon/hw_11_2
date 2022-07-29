import json
from setings import PATCH_CANDIDATES_JSON


def load_candidates_from_json() -> list[dict]:
    """
    Загружаем список кандидатов и информацию о них из файла
    :return:
    """
    with open(PATCH_CANDIDATES_JSON, encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id: int) ->dict:
    """
    На странице /candidates/<pk> выводим информацию о кандидате по его id
    :return:
    """
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    result = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == int(candidate_name):
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name: str) -> list[dict]:
    result = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result


@app.route('/')
def get_all(candidates=load_candidates_from_json()):
    """
     На главной странице выводим список всех кандитатов
    :return:
    """
    return render_template('list.html', candidates=candidates)



