#Project 2 Full-Stack ND (Udacity)
##Tournament
This is a project to introduce how to use the relational database in Postgresql and python.The project is to generate tables and functions to a tournament and pass successfull all tests.

**This project is based on the Tournament created by Udacity-Team
for the course "Intro to Relational Databases".**

### Tech

* [Psycopg] - Psycopg is the most popular PostgreSQL adapter for the Python programming language.

### Requeriments

Installs the following:

- Python 2.7.6
- Postgresql 9.3.6

### What's included

Within the download you'll find the following directories and files.
You'll see something like this:

```
Tournament/
├── README.md
├── tournament.py
├── tournament.sql
├── tournament_test.py
└──README.md
```

### Instrucctions

#####1.- Create the databases
To create the database with all tables and views, we need go to Command Line to enter to psql using the following code:
```sh
$ psql
```
inside of the psql command line we need to use the following codes for create the databases with all tables and views
```sh
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament
\i tournament.sql
```

To test all function we need out from the psql command line with the following code:
```sh
\q
```
And for test all function we need use this code:
```sh
$ python tournament_test.py
```
And the 10 tests must be passed.

### Author

**Rodolfo Lugo**

- [LikedIn]


[Psycopg]:http://initd.org/psycopg/
[LikedIn]:https://www.linkedin.com/pub/rodolfo-edu-lugo-garcia/8a/b03/195