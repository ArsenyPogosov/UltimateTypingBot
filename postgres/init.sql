CREATE TABLE IF NOT EXISTS scores (
    id BIGINT,
    username TEXT,
    score_small BIGINT,
    score_medium BIGINT,
    score_large BIGINT,
    is_public BOOLEAN,
    UNIQUE (id)
);
