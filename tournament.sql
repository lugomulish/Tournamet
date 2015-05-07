-- Table definitions for the tournament project.
--
--In the psql console you can connect to the foo database by typing the following code:
--
--1.-"drop database if exists tournament;"
--2.-"create database tournament;"
--3.-"\c tournament"
--4.-"\i tournament.sql"


CREATE TABLE players ( name TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL PRIMARY KEY);

CREATE TABLE tournaments ( name TEXT,
                     description TEXT,
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


