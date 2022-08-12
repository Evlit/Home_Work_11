# Домашка к уроку 10.2
# Основной модуль запуска декораторов
from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

data = load_candidates_from_json("candidates.json")
app = Flask(__name__)


@app.route("/")
def page_index():
    """
    Деоратор без параметров -вывод всего списка кандидатов
    """
    return render_template('list.html', items=data)


@app.route('/candidate/<int:id_>')
def get_user(id_):
    """
    Вывод одного кандидата по номеру
    """
    user = get_candidate(id_, data)
    return render_template('card.html', item=user)


@app.route('/search/<candidate_name>')
def search_user(candidate_name):
    """
    Вывод одного кандидата по имени
    """
    user = get_candidates_by_name(candidate_name, data)
    count_users = len(user)
    return render_template('search.html', items=user, count_users=count_users)


@app.route('/skill/<skill_name>')
def search_skill(skill_name):
    """
    Вывод кандидатов по навыку
    """
    user = get_candidates_by_skill(skill_name.lower(), data)
    count_users = len(user)
    return render_template('skill.html', items=user, count_users=count_users, skill=skill_name)


if __name__ == '__main__':
    app.run(port=5000)
