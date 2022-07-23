import json
from flask import Flask, render_template, request

app = Flask(__name__)


def load_candidates_from_json(path):
    """
    Загружаем список кандидатов и информацию о них из файла
    :return:
    """
    with open(path, encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def get_candidate(candidate_id: str, candidates):
    """
    На странице /candidates/<pk> выводим информацию о кандидате по его id
    :return:
    """
    for candidate in candidates:
        if candidate['id'] == int(candidate_id):
            return f"""
                    <pre>
                    <img src="({candidate['picture']})">
                    Имя кандидата: {candidate['name']}
                    Позиция кандидата: {candidate['position']}
                    Навыки кандидата: {candidate['skills'].lower()}
                    </pre>
                    """


def get_candidates_by_name(candidate_name, candidates ):
    for candidate in candidates:
        if candidate['name'] == int(candidate_name):
            return f"""
                    <pre>
                    <img src="({candidate['picture']})">
                    Имя кандидата: {candidate['name']}
                    Пол: {candidate['gender']}
                    Возраст: {candidate['age']}
                    Позиция кандидата: {candidate['position']}
                    Навыки кандидата: {candidate['skills'].lower()}
                    </pre>
                    """


def get_candidates_by_skill(skill_name, candidates):
    result = ''
    for candidate in candidates:
        if skill_name in candidate['skills']:
            result += f"""
                        <pre>
                        Имя кандидата: {candidate['name']}
                        Позиция кандидата: {candidate['position']}
                        Навыки кандидата: {candidate['skills'].lower()}
                        </pre>
                        \n\t
                        """
    return result


@app.route('/')
def get_all(candidates):
    """
     На главной странице выводим список всех кандитатов
    :return:
    """
    return render_template('list.html', candidates=candidates)

app.run()

