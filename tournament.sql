-- Table definitions for the tournament project.
--
--In the psql console you can connect to the foo database by typing the following code:
--
--1.-"drop database if exists tournament;"
--2.-"create database tournament;"
--3.-"\c tournament"
--4.-"\i tournament.sql"

--tournanments table create script.In this table to be registered all tournaments.
CREATE TABLE tournaments ( name TEXT,
                     description TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     id SERIAL PRIMARY KEY);

--players table create script.In this table to be registered all player of the tournaments.
--This table contains a foreign key reference to tournaments table(tournament_id)
CREATE TABLE players ( name TEXT,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                     tournament_id INTEGER REFERENCES tournaments(id),
                     id SERIAL PRIMARY KEY);

--matches table create script. In this table to be registered all matches for every tournament.
--This table contains a foreign key reference to tournaments table(tournament_id)
CREATE TABLE matches (winner INTEGER REFERENCES players(id),
                      loser INTEGER REFERENCES players(id),
                      tournament_id INTEGER REFERENCES tournaments(id),
                       id SERIAL PRIMARY KEY );

--Create Player standings view.This view contains the id, name, winner, matches and tournament_id.
CREATE VIEW playerStandings
                      AS SELECT  players.tournament_id, players.id, players.name, (SELECT COUNT (*)
                      FROM Matches WHERE Matches.winner = players.id)
                      AS winner, (SELECT COUNT(*) FROM Matches
                      where Matches.winner = players.id OR Matches.loser = players.id)
                      AS matches FROM players LEFT JOIN Matches
                      ON players.id = Matches.winner OR players.id = Matches.loser
                      GROUP BY players.id ORDER BY winner DESC;