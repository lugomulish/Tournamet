-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE players ( name TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL PRIMARY KEY);

CREATE TABLE tournament ( name TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL PRIMARY KEY);

CREATE TABLE Matches (winner INTEGER REFERENCES players(id),
                      loser INTEGER REFERENCES players(id),
                       id SERIAL PRIMARY KEY )

