from components.init_postgres import db

import logging

def init_user(id, username):
    try:
        db.execute(f"""
    INSERT INTO scores (id, username, score_small, score_medium, score_large, is_public) 
    VALUES ({id}, '{username}', NULL, NULL, NULL, FALSE);
    """)
    except:
        logging.info(f"User {id} already exists in postgres")

def change_user_field(id, field_name, field_value):
    db.execute(f"""
    UPDATE scores
    SET {field_name} = {field_value}
    WHERE id = {id};
    """)

def read_user_field(id, field_name):
    response = db.execute(f"""
    SELECT {field_name}
    FROM scores
    WHERE id = {id};
    """)
    for (r) in response:
        return r[0]

def get_user_scores(id):
    return [read_user_field(id, 'score_small'), read_user_field(id, 'score_medium'), read_user_field(id, 'score_large')]

def get_best(field_name, n):
    response = db.execute(f"""
    SELECT *
    FROM scores
    WHERE is_public
    ORDER BY {field_name} ASC
    LIMIT {n};
    """)
    return [[row["username"], row["score_small"], row["score_medium"], row["score_large"]] for row in response]
