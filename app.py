from flask import Flask
import utils
app = Flask(__name__)


@app.route('/')
def all_candidates():
    candidates = utils.load_candidates()
    return utils.build_html_more_candidates(candidates)

@app.route('/candidate/<int:pk>')
def candidate_page(pk):
    candidate = utils.get_candidate_by_id(pk)
    if candidate is None:
        return "<pre>Такого кандидата нет</pre>"
    return utils.build_html_one_candidate(candidate)

@app.route('/skills/<skill>')
def skills_page(skill):
    candidates_skills = utils.get_candidates_by_skill(skill)
    if len(candidates_skills) == 0:
        return "<pre>Кандидатов с таким умением нет</pre>"
    return utils.build_html_more_candidates(candidates_skills)

if __name__ == '__main__':
    app.run()
