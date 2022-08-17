from flask import Flask, render_template
from pip._internal.resolution.resolvelib import candidates

import utils

utils.load_candidates_from_json()

app = Flask(__name__, template_folder="templates")

@app.route("/")
def page_index():
    candidates=utils.load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:x>")
def page_candidate(x):
  cand_by_id = utils.get_candidate(x)
  page = render_template("card.html", cand_by_id=cand_by_id)
  return page

@app.route("/search/<candidate_name>/")
def page_name(candidate_name):
    candidates = utils.load_candidates_from_json()
    cands_by_name = utils.get_candidates_by_name(candidate_name)
    len_cands = len(utils.get_candidates_by_name(candidate_name))
    page = render_template("search.html", cands_by_name=cands_by_name, len_cands=len_cands)
    return page

@app.route("/skill/<skill_name>")
def page_skills(skill_name):
    candidates = utils.load_candidates_from_json()
    cands_by_skills = utils.get_candidates_by_skill(skill_name)
    page = render_template("skill.html", cands_by_skills=cands_by_skills)
    return page

if __name__ == "__main__":
    app.run()
