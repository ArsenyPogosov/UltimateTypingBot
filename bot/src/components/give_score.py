from Levenshtein import distance

def give_score(task, message, time):
    if 'o' in message or 'c' in message:
        return [99999, "cheating = "]
    errors = distance(' '.join(task), message) 
    time = int(time)
    return [time + errors * 5, f"{time} + {errors} * 5 = "]
