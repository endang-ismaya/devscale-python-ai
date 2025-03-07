def is_ready_to_kaburajadulu(
    age: int, can_speak_english: str, having_dev_skills: str
) -> str:
    is_english = can_speak_english == "Yes"
    is_dev_skills = having_dev_skills == "Yes"

    if age > 17 and is_english and is_dev_skills:
        return "You are ready to #kaburajadulu"

    elif age < 18 and not is_english and not is_dev_skills:
        return "You must greater than 17 years old!, can speak english, and have dev skills!"

    elif age < 18:
        return "You need to grow up first :D"

    elif not is_english:
        return "Please learn english first!"

    else:
        return "You must have dev skills!"
