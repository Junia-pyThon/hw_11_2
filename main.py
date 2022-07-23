from setings import PATCH_CANDIDATES_JSON
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill, get_all


list_candidates = load_candidates_from_json(PATCH_CANDIDATES_JSON)
get_all(list_candidates)
