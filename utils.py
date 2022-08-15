import json



def load_candidates_from_json():
  """возвращает список всех кандидатов"""
  global candidates
  with open("candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)
  return candidates

def get_candidate(candidate_id):
  """возвращает одного кандидата по его id"""
  for item in candidates:
    if item["id"] == candidate_id:
      candidate_by_id = item
  return candidate_by_id

def get_candidates_by_name(candidate_name):
  """возвращает кандидатов по имени"""
  candidate_by_name = []
  for item in candidates:
    if candidate_name in item["name"]:
      candidate_by_name.append(item)
  return candidate_by_name

def get_candidates_by_skill(skill_name):
  """возвращает кандидатов по навыку"""
  candidates_by_skill = []
  for item in candidates:
    if skill_name in item["skills"]:
      candidates_by_skill.append(item)
  return candidates_by_skill


