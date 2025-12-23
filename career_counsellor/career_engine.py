from careers_data import CAREERS

def score_career(user_profile, career):
    skill_score = len(set(user_profile["skills"]) & set(career["skills"]))
    interest_score = 2 if user_profile["interest"] in career["interest"] else 0
    market_score = career["demand"]

    return skill_score * 3 + interest_score * 2 + market_score

def recommend_careers(user_profile, top_n=2):
    scored = []
    for career in CAREERS:
        score = score_career(user_profile, career)
        scored.append((career, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]
