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
query = "select player_id from bowlers_attr where innings >50 and bowling_average >30"
cur.execute(query)
rows = cur.fetchall()
length_players = rows.length
query1 ="select country,player_id from players_attr where player_id in rows" 
cur.execute(query1)
final_rows = cur.fetchall()
adj_mat = build_adjacencymatrix(final_rows)
	