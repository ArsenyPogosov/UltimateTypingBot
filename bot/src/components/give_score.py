from Levenshtein import distance

def give_score(task, message, time):
    errors = distance(' '.join(task), message) 
    time = int(time)
    return [time + errors * 5, f"{time} + {errors} * 5 = "]
