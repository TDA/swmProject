import MySQLdb as mdb
import glob
import adjacency
from xml.dom import minidom

def getopenconnection(host='localhost', user='root', password='jaswi!23', dbname='swmproject'):
    return mdb.connect(host=host,  # your host, usually localhost
                           user=user,  # your username
                           passwd=password,  # your password
                           db=dbname)  # name of the data base

db= getopenconnection()
print db
cur= db.cursor()
cur1= db.cursor()
cur2=db.cursor()
cur3=db.cursor()
query_bowlers = "select player_id from bowlers_attr where innings >30 and bowling_average <30 and economy < 5.25 and strike_rate < 35 and wickets >50"
query_batsmen = "select player_id from batsmen_attr where matches > 20 and innings >15 and batting_average > 35 and runs/balls_taken > 0.80 and centuries > 5 and half_centuries > 10"
query_allrounder = "select p.player_id from batsmen_attr p,bowlers_attr b where p.player_id=b.player_id and p.matches>20 and p.innings > 20 and p.batting_average >20 and p.runs/balls_taken > 0.70 and p.half_centuries >5 and b.bowling_average <40 and b.strike_rate <45 and b.wickets >5" 
query_wicketkeeper = "select player_id from batsmen_attr where matches > 20 and innings > 15 and stumpings > 5 and catches > 75"
cur.execute(query_bowlers)
cur1.execute(query_batsmen)
cur2.execute(query_allrounder)
cur3.execute(query_wicketkeeper)
rows_bowlers = cur.fetchall()
rows_batsmen= cur1.fetchall()
rows_allrounder=cur2.fetchall()
rows_wicketkeeper = cur3.fetchall()
length_players_bowlers = len(rows_bowlers)
length_players_batsmen = len(rows_batsmen)
length_players_allrounder = len(rows_allrounder)
length_players_wicketkeeper = len(rows_wicketkeeper)
query1 ="select country,player_id from player_attr where player_id in (%s)"
ids_bowlers= [(str(i).split("'")[1]).split(",")[0] for i in rows_bowlers]
ids_batsmen= [(str(i).split("'")[1]).split(",")[0] for i in rows_batsmen]
ids_allrounder= [(str(i).split("'")[1]).split(",")[0] for i in rows_allrounder]
ids_wicketkeeper= [(str(i).split("'")[1]).split(",")[0] for i in rows_wicketkeeper]
in_bowlers=', '.join(list(map(lambda x: '%s', ids_bowlers)))
in_batsmen=', '.join(list(map(lambda x: '%s', ids_batsmen)))
in_allrounder=', '.join(list(map(lambda x: '%s', ids_allrounder)))
in_wicketkeeper=', '.join(list(map(lambda x: '%s', ids_wicketkeeper)))

query0 = query1 % in_bowlers
query2 = query1 % in_batsmen
query3 = query1 % in_allrounder
query4 = query1 % in_wicketkeeper
cur.execute(query0,ids_bowlers)
cur1.execute(query2,ids_batsmen)
cur2.execute(query3,ids_allrounder)
cur3.execute(query4,ids_wicketkeeper)
final_rows_bowlers = cur.fetchall()
final_rows_batsmen = cur1.fetchall()
final_rows_allrounder = cur2.fetchall()
final_rows_wicketkeeper = cur3.fetchall()
print 'LIST OF BATSMEN AFTER DECISION TREE'
for i in final_rows_batsmen:
    print i
print '\n'
print 'LIST OF BOWLERS AFTER DECISION TREE'
for i in final_rows_bowlers:
    print i
print '\n'
print 'LIST OF ALLROUNDERS AFTER DECISION TREE'
for i in final_rows_allrounder:
    print i
print '\n'
print 'LIST OF wicketkeepers AFTER DECISION TREE'
for i in final_rows_wicketkeeper:
    print i
print '\n'
adj_mat_bowlers = adjacency.build_adjacencymatrix(list(final_rows_bowlers))
adj_mat_batsmen = adjacency.build_adjacencymatrix(list(final_rows_batsmen))
adj_mat_allrounder = adjacency.build_adjacencymatrix(list(final_rows_allrounder))
adj_mat_wicketkeeper = adjacency.build_adjacencymatrix(list(final_rows_wicketkeeper))
print 'BATSMEN_ADJACENY MATRIX'
print adj_mat_bowlers
print 'BOWLERS ADJACENCY MATRIX'
print adj_mat_batsmen
print  'ALLROUNDER ADJACENCY MATRIX'
print adj_mat_allrounder
print 'ADJACENCY MATRIX FOR WICKETKEEPERS'
print adj_mat_wicketkeeper
	