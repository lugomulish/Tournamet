#!/usr/bin/env python
# Test cases for tournament.py

from tournament import *


def test_delete_matches():
    delete_matches()
    print "1. Old matches can be deleted."


def test_delete():
    delete_matches()
    delete_players()
    print "2. Player records can be deleted."


def test_count():
    delete_matches()
    delete_players()
    c = count_players()
    if c == '0':
        raise TypeError(
            "countPlayers() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "3. After deleting, countPlayers() returns zero."


def test_register():
    delete_matches()
    delete_players()
    register_tournament("SuperTorneo", "Torneo de Halo")
    tournament_id = get_last_tournament_id()
    register_player("Chandra Nalaar", tournament_id)
    c = count_players()
    if c != 1:
        raise ValueError(
            "After one player registers, countPlayers() should be 1.")
    print "4. After registering a player, countPlayers() returns 1."


def test_register_count_delete():
    delete_matches()
    delete_players()
    register_tournament("SuperTorneo", "Torneo de Halo")
    tournament_id = get_last_tournament_id()
    register_player("Markov Chaney", tournament_id)
    register_player("Joe Malik", tournament_id)
    register_player("Mao Tsu-hsi", tournament_id)
    register_player("Atlanta Hope", tournament_id)
    c = count_players()
    if c != 4:
        raise ValueError(
            "After registering four players, countPlayers should be 4.")
    delete_players()
    c = count_players()
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "5. Players can be registered and deleted."


def test_standings_before_matches():
    delete_matches()
    delete_players()
    register_tournament("SuperTorneo", "Torneo de Halo")
    tournament_id = get_last_tournament_id()
    register_player("Melpomene Murray", tournament_id)
    register_player("Randy Schwartz", tournament_id)
    standings = player_standings(tournament_id)
    if len(standings) < 2:
        raise ValueError("Players should appear in playerStandings even before"
                         "they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 5:
        raise ValueError("Each playerStandings row should have four columns.")
    [(tournament_id, id1, name1, wins1, matches1),
     (tournament_id, id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in standings"
                         ", even if they have no matches played.")
    print "6.Newly registered players appear in the standings with no matches."


def test_report_matches():
    delete_matches()
    delete_players()
    register_tournament("SuperTorneo", "Torneo de Halo")
    tournament_id = get_last_tournament_id()
    register_player("Bruno Walton", tournament_id)
    register_player("Boots O'Neal", tournament_id)
    register_player("Cathy Burton", tournament_id)
    register_player("Diane Grant", tournament_id)
    standings = player_standings(tournament_id)
    [id1, id2, id3, id4] = [row[1] for row in standings]
    report_match(id1, id2, tournament_id)
    report_match(id3, id4, tournament_id)
    standings = player_standings(tournament_id)
    for (t, i, n, w, m) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win"
                             "recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins"
                             "recorded.")
    print "7. After a match, players have updated standings."


def test_pairings():
    delete_matches()
    delete_players()
    register_tournament("SuperTorneo", "Torneo de Halo")
    tournament_id = get_last_tournament_id()
    register_player("Twilight Sparkle", tournament_id)
    register_player("Fluttershy", tournament_id)
    register_player("Applejack", tournament_id)
    register_player("Pinkie Pie", tournament_id)
    standings = player_standings(tournament_id)
    [id1, id2, id3, id4] = [row[1] for row in standings]
    report_match(id1, id2, tournament_id)
    report_match(id3, id4, tournament_id)
    pairings = swiss_pairings(tournament_id)
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swissPairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "8. After one match, players with one win are paired."


def test_register_tournament():
    delete_all_tournaments()
    register_tournament("SuperTorneo", "Torneo de Halo")
    c = count_tournaments()
    if c != 1:
        raise ValueError(
            "After one tournament registers, countTournaments() should be 1.")
    print "9. After registering a tournament, countTournaments() returns 1."


def test_delete_tournaments():
    register_tournament("SuperTorneo", "Torneo de Halo")
    delete_all_tournaments()
    c = count_tournaments()
    if c != 0:
        raise ValueError(
            "After one tournament registers, countTournaments() should be 0.")
    print "10. After registering a tournament, countTournaments() returns 0."


def test_count_players_from_tournament():
    delete_matches()
    delete_all_tournaments()
    register_tournament("SuperTorneo", "Torneo de Halo")
    tournament_id = get_last_tournament_id()
    register_player("Twilight Sparkle", tournament_id)
    register_player("Rodolfo Lugo", tournament_id)
    register_player("Stephanie Cocom", tournament_id)
    register_player("Angel Lugo", tournament_id)
    c = count_players_from_tournament(tournament_id)
    if c != 4:
        raise ValueError("After registering, count_players_from_tournament()"
                         " should return 4.")
    print "11. After registering, count_players_from_tournament() returns 4."


def test_delete_tournament():
    delete_matches()
    delete_all_tournaments()
    register_tournament("SuperTorneo", "Torneo de Halo")
    tournament_id = get_last_tournament_id()
    delete_tournament(tournament_id)
    c = count_tournaments()
    if c != 0:
        raise ValueError("After one tournament deleting, countTournaments()"
                         " should be 0.")
    print "12. After one tournament deleting, countTournaments() return 0."


def test_delete_players_from_tournament():
    delete_matches()
    delete_players()
    register_tournament("SuperTorneo", "Torneo de Halo")
    tournament_id = get_last_tournament_id()
    delete_players_from_tournament(tournament_id)
    c = count_players_from_tournament(tournament_id)
    if c != 0:
        raise ValueError("After delete_players_from_tournament, "
                         "count_players_from_tournament() should be 0.")
    print "13. After delete_players_from_tournament, " \
          "count_players_from_tournament() return 0."


if __name__ == '__main__':
    test_delete_matches()
    test_delete()
    test_count()
    test_register()
    test_register_count_delete()
    test_standings_before_matches()
    test_report_matches()
    test_pairings()
    test_register_tournament()
    test_delete_tournaments()
    test_count_players_from_tournament()
    test_delete_tournament()
    test_delete_players_from_tournament()

    print "Success!  All tests pass!"
