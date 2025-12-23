def update_profile(profile, user_input):
    text = user_input.lower()

    if "tech" in text:
        profile["interest"] = "tech"
    elif "art" in text or "design" in text:
        profile["interest"] = "arts"
    elif "business" in text or "commerce" in text:
        profile["interest"] = "commerce"

    skills_map = ["python", "java", "design", "statistics", "seo"]
    for skill in skills_map:
        if skill in text:
            profile["skills"].append(skill)

    return profile
