from components import scores

def update_score(userid, task_type, score):
    field_name = "score_" + task_type.name.lower()
    record = scores.read_user_field(userid, field_name)
    if record is None or record > score:
        scores.change_user_field(userid, field_name, str(score))
        return True

    return False
