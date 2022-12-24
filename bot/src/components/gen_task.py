import random
import logging

words = open("data/words.txt", 'r').read().split('\n')

def gen_task(symb_count):
    result = []
    length = -1
    while length < symb_count:
        new_word = random.choice(words)
        result.append(new_word)
        length += len(new_word) + 1

    logging.info("Generate task: " + str(result))
    return result
