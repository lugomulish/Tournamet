#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.
    Returns a database connection and the cursor."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Unable to connect to database")


def delete_matches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    query = "TRUNCATE matches CASCADE"
    cursor.execute(query)
    db.commit()
    db.close()


def delete_players():
    """Remove all the player records from the database."""
    db, cursor = connect()
    query1 = "TRUNCATE players CASCADE"
    query2 = "TRUNCATE tournaments CASCADE"
    cursor.execute(query1)
    cursor.execute(query2)
    db.commit()
    db.close()


def register_tournament(name, description):
    """Register a new tournament in the database."""
    db, cursor = connect()
    query = "INSERT INTO tournaments (name, description) VALUES (%s,%s)"
    params = (name, description,)
    cursor.execute(query, params)
    db.commit()
    db.close()


def count_tournaments():
    """Returns the number of tournaments currently registered."""
    db, cursor = connect()
    query = "SELECT COUNT(*) FROM tournaments"
    cursor.execute(query)
    count = cursor.fetchall()[0][0]
    db.close()
    return count


def delete_all_tournaments():
    """Remove all the tournaments records from the database."""
    db, cursor = connect()
    query = "TRUNCATE tournaments CASCADE"
    cursor.execute(query)
    db.commit()
    db.close()


def delete_tournament(id):
    """Remove all the tournaments records from the database."""
    db, cursor = connect()
    query = "DELETE FROM tournaments WHERE id = (%s) CASCADE"
    params = (id,)
    cursor.execute(query, params)
    db.commit()
    db.close()


def count_players():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    query = "SELECT COUNT(*) FROM players"
    cursor.execute(query)
    count = cursor.fetchall()[0][0]
    db.close()
    return count


def register_player(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    query = "INSERT INTO players (name) VALUES (%s)"
    params = (name,)
    cursor.execute(query, params)
    db.commit()
    db.close()


def player_standings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    query = "SELECT * FROM playerStandings"
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results


def report_match(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    query = "INSERT INTO matches (winner, loser) VALUES (%s,%s)"
    params = (winner, loser,)
    cursor.execute(query, params)
    db.commit()
    db.close()


def swiss_pairings():
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
    players_list = player_standings()

    for index, player in enumerate(players_list):
        if index % 2 == 0:
            match = (players_list[index][0], players_list[index][1],
                     players_list[index + 1][0], players_list[index + 1][1])
            results.append(match)
    return results
