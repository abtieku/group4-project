-- possible error with forien key in join function

CREATE TABLE business_table (
    business_id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    address VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    state VARCHAR NOT NULL,
    postal_code VARCHAR NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    stars FLOAT NOT NULL,
    review_count INT NOT NULL,
    is_open INT NOT NULL
);

CREATE TABLE review_table (
    review_id VARCHAR PRIMARY KEY,
    user_id VARCHAR NOT NULL,
    business_id VARCHAR REFERENCES business_table (business_id),
    stars INT NOT NULL,
    useful INT NOT NULL,
    funny INT NOT NULL,
    cool INT NOT NULL,
    text VARCHAR NOT NULL,
    date DATE NOT NULL
);


