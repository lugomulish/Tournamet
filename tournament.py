#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("TRUNCATE matches CASCADE")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("TRUNCATE players CASCADE")
    c.execute("TRUNCATE tournaments CASCADE")
    DB.commit()
    DB.close()


def registerTournament(name, description):
    """Register a new tournament in the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO tournaments (name, description) VALUES (%s,%s)", (name, description,))
    DB.commit()
    DB.close()

def countTournaments():
    """Returns the number of tournaments currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("SELECT COUNT(*) FROM tournaments")
    count = c.fetchall()[0][0]
    db.close()
    return count

def deleteAllTournaments():
    """Remove all the tournaments records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("TRUNCATE tournaments CASCADE")
    DB.commit()
    DB.close()

def deleteTournament(id):
    """Remove all the tournaments records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM tournaments WHERE id = (%s) CASCADE", (id,))
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("SELECT COUNT(*) FROM players")
    count = c.fetchall()[0][0]
    db.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM playerStandings")
    results = c.fetchall()
    db.close()
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s,%s)", (winner, loser,))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    results = list()
    playersList = playerStandings()

    for index,player in enumerate(playersList):
        if index % 2 == 0:
            match = (playersList[index][0], playersList[index][1],
                     playersList[index+1][0], playersList[index+1][1])
            results.append(match)
    return results



