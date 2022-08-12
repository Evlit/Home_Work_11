# Домашка к уроку 10.2
# Модуль описания функций
import json
from Aplicant import Applicant2


def load_candidates_from_json(file):
    """
    Загрузка из jason файла
    """
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    candidates = []
    for candidate in data:
        candidates.append(Applicant2(candidate['id'], candidate['name'], candidate['picture'], candidate['position'],
                                     candidate['gender'], candidate['age'], candidate['skills'].lower()))
    return candidates


def get_candidate(id_, candidates):
    """
    Получение кандидата по номеру
    """
    for candidate in candidates:
        if candidate.id == id_:
            return candidate


def get_candidates_by_skill(skill_name, candidates):
    """
    Получение списка кандидатов по навыку
    """
    candidate_skills = []
    for candidate in candidates:
        if skill_name in candidate.skills:
            candidate_skills.append(candidate)
    return candidate_skills


def get_candidates_by_name(name, candidates):
    """
    Получение списка кандидатов по навыку
    """
    candidate_names = []
    for candidate in candidates:
        if name in candidate.name:
            candidate_names.append(candidate)
    return candidate_names
