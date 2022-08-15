from flask import Flask, render_template
import utils

utils.load_candidates_from_json()

app = Flask(__name__)

@app.route("/")
def page_index(candidates):
   return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int: x>")
def page_candidate(x):
  cand_by_id = utils.get_candidate(x)
  page = render_template("card.html", cand_by_id=cand_by_id)
  return page

@app.route("/search/<candidate_name>")
def page_name(candidate_name):
    cands_by_name = utils.get_candidates_by_name(candidate_name)
    page = render_template("search.html", cands_by_name=cands_by_name)
    return page

@app.route("/search/<skill_name>")
def page_skills(skill_name):
    cands_by_skills = utils.get_candidates_by_skill(skill_name)
    page = render_template("skill.html", cands_by_skills=cands_by_skills)
    return page

app.run()