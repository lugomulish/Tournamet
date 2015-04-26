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

CREATE TABLE matches (winner INTEGER REFERENCES players(id),
                      loser INTEGER REFERENCES players(id),
                       id SERIAL PRIMARY KEY );

CREATE VIEW playerStandings
                      AS SELECT players.id, players.name, (SELECT COUNT (*)
                      FROM Matches WHERE Matches.winner = players.id)
                      AS winner, (SELECT COUNT(*) FROM Matches
                      where Matches.winner = players.id OR Matches.loser = players.id)
                      AS matches FROM players LEFT JOIN Matches
                      ON players.id = Matches.winner OR players.id = Matches.loser
                      GROUP BY players.id ORDER BY winner DESC;


