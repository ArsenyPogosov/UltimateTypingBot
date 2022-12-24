from components.init_postgres import db

import logging

def init_user(username):
    db.execute(f"""
    INSERT INTO scores (username, score_small, score_medium, score_large, is_public) 
    VALUES ('{username}', NULL, NULL, NULL, TRUE);
    """)

def change_user_field(username, field_name, field_value):
    db.execute(f"""
    UPDATE scores
    SET {field_name} = {field_value}
    WHERE username = '{username}';
    """)

def read_user_field(username, field_name):
    response = db.execute(f"""
    SELECT {field_name}
    FROM scores
    WHERE username = '{username}'
    """)
    for (r) in response:
        return r[0]

def get_user_scores(username):
    return [read_user_field(username, 'score_small'), read_user_field(username, 'score_medium'), read_user_field(username, 'score_large')]

def get_best(field_name, n):
    query = f"""
    SELECT score_small
    FROM scores
    WHERE username = '{username}'
    """
    result_set = db.execute(query)  
    for (r) in result_set:  
        return r[0]

