import json
from setings import PATCH_CANDIDATES_JSON


def load_candidates_from_json() -> list[dict]:
    with open(PATCH_CANDIDATES_JSON, encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id: int) ->dict:
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






