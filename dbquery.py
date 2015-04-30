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
length_players = len(rows)
query1 ="select country,player_id from player_attr where player_id in (%s)"
ids= [(str(i).split("'")[1]).split(",")[0] for i in rows]
in_p=', '.join(list(map(lambda x: '%s', ids)))
query1 = query1 % in_p
cur.execute(query1,ids)
final_rows = cur.fetchall()
adj_mat = adjacency.build_adjacencymatrix(list(final_rows))
print adj_mat
	