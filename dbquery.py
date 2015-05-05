import MySQLdb as mdb
import glob
import adjacency
from selection_process import *
from xml.dom import minidom

def getopenconnection(host='localhost', user='root', password='jaswi!23', dbname='swmproject'):
    return mdb.connect(host=host,  # your host, usually localhost
                           user=user,  # your username
                           passwd=password,  # your password
                           db=dbname)  # name of the data base

def compute_avg(list_p):
    sum=0
    for x in list_p:
        sum+=x
    return round(sum/len(list_p),0)



db= getopenconnection()
print db
cur= db.cursor()
cur1= db.cursor()
cur2=db.cursor()
cur3=db.cursor()
cur4=db.cursor()
input =[[2,'right-arm medium',3],[2,'left-arm fast',2],[1,'right',4],[3,'fff',1]]
batsmen_rank_list=[]
bowlers_rank_list=[]
allrounder_rank_list=[]
final_players=[]
batsmen_count =0
bowlers_count =0
allrounders_count = 0
for i in input:
    print i
    if i[0] == 1:
        batsmen_count += i[2]
    elif i[0]==2:
        bowlers_count += i[2]
    else:
        allrounders_count += i[2]
query1 ="select country,player_id from player_attr where player_id in (%s)"

query_bowlers = "select b.player_id from bowlers_attr b,player_attr p where b.player_id = p.player_id and b.innings >30 and b.bowling_average <30 and b.economy < 5.25 and b.strike_rate < 35 and b.wickets >50"
cur.execute(query_bowlers)
rows_bowlers = cur.fetchall()
length_players_bowlers = len(rows_bowlers)
ids_bowlers= [(str(j).split("'")[1]).split(",")[0] for j in rows_bowlers]
in_bowlers=', '.join(list(map(lambda x: '%s', ids_bowlers)))
query0 = query1 % in_bowlers
cur.execute(query0,ids_bowlers)

query_batsmen = "select player_id from batsmen_attr where matches > 20 and innings >15 and batting_average > 35 and runs/balls_taken > 0.80 and centuries > 5 and half_centuries > 10"
cur1.execute(query_batsmen)
rows_batsmen= cur1.fetchall()
length_players_batsmen = len(rows_batsmen)
ids_batsmen= [(str(i).split("'")[1]).split(",")[0] for i in rows_batsmen]
in_batsmen=', '.join(list(map(lambda x: '%s', ids_batsmen)))
query2 = query1 % in_batsmen
cur1.execute(query2,ids_batsmen)


query_allrounder = "select p.player_id from batsmen_attr p,bowlers_attr b where p.player_id=b.player_id and p.matches>20 and p.innings > 20 and p.batting_average >20 and p.runs/balls_taken > 0.70 and p.half_centuries >5 and b.bowling_average <40 and b.strike_rate <45 and b.wickets >5" 
cur2.execute(query_allrounder)
rows_allrounder=cur2.fetchall()
length_players_allrounder = len(rows_allrounder)
ids_allrounder= [(str(i).split("'")[1]).split(",")[0] for i in rows_allrounder]
in_allrounder=', '.join(list(map(lambda x: '%s', ids_allrounder)))
query3 = query1 % in_allrounder
cur2.execute(query3,ids_allrounder)

query_wicketkeeper = "select player_id from batsmen_attr where matches > 20 and innings > 15 and stumpings > 5 and catches > 75"
cur3.execute(query_wicketkeeper)
rows_wicketkeeper = cur3.fetchall()
length_players_wicketkeeper = len(rows_wicketkeeper)
ids_wicketkeeper= [(str(i).split("'")[1]).split(",")[0] for i in rows_wicketkeeper]
in_wicketkeeper=', '.join(list(map(lambda x: '%s', ids_wicketkeeper)))
query4 = query1 % in_wicketkeeper
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
print adj_mat_batsmen
print 'BOWLERS ADJACENCY MATRIX'
print adj_mat_bowlers
print  'ALLROUNDER ADJACENCY MATRIX'
print adj_mat_allrounder
print 'ADJACENCY MATRIX FOR WICKETKEEPERS'
print adj_mat_wicketkeeper

for i in list(final_rows_batsmen):
    print i[1]
    batsmen_rank = "select batting_rank from main where player_id ='"+str(i[1])+"'"
    cur4.execute(batsmen_rank)
    batsmen_rank_final = cur4.fetchall()[0][0]
    print batsmen_rank_final
    batsmen_rank_list.append(batsmen_rank_final)
print batsmen_rank_list

for i in list(final_rows_bowlers):
    print i[1]
    bowlers_rank = "select bowling_rank from main where player_id ='"+str(i[1])+"'"
    cur4.execute(bowlers_rank)
    bowlers_rank_final = cur4.fetchall()[0][0]
    bowlers_rank_list.append(bowlers_rank_final)
print bowlers_rank_list

for i in list(final_rows_allrounder):
    print i[1]
    allrounder_rank = "select allrounder_rank from main where player_id ='"+str(i[1])+"'"
    cur4.execute(allrounder_rank)
    allrounder_rank_final = cur4.fetchall()[0][0]
    allrounder_rank_list.append(allrounder_rank_final)
print allrounder_rank_list
print return_players(adj_mat_bowlers,bowlers_rank_list,bowlers_count)
print return_players(adj_mat_batsmen,batsmen_rank_list,batsmen_count)
print return_players(adj_mat_allrounder,allrounder_rank_list, allrounders_count)


final_batting_ranks=list()
for i in return_players(adj_mat_batsmen,batsmen_rank_list,batsmen_count):
    final_players.append(list(final_rows_batsmen)[i][1])
    final_batting_ranks.append(batsmen_rank_list[i])
print final_batting_ranks
b_rank_avg=compute_avg(final_batting_ranks)

final_bowling_ranks=list()
final_players.append('36e136fe-f2dc-4115-9d55-c808598fab5a')
for i in return_players(adj_mat_bowlers,bowlers_rank_list,bowlers_count):
    final_players.append(list(final_rows_bowlers)[i][1])
    final_bowling_ranks.append(bowlers_rank_list[i])
    
bo_rank_avg=compute_avg(final_bowling_ranks)

final_allrounder_ranks=list()    
for i in return_players(adj_mat_allrounder,allrounder_rank_list, allrounders_count):
    final_players.append(list(final_rows_allrounder)[i][1])
    final_allrounder_ranks.append(allrounder_rank_list[i])
    
for x in final_players:
    print x
a_rank_avg=compute_avg(final_allrounder_ranks)
with open("output.txt","w") as file:
    file.write('FINAL TEAM PLAYERS')
    print 'FINAL TEAM PLAYERS'
    print '\n'
    print '\n'
    file.write('\n')
    file.write('\n')
    for i in final_players:
        
        query_final="select full_name from main where player_id= '"+ str(i) +"'"
        cur.execute(query_final)
        row=cur.fetchall()[0][0]
        print row
        file.write(row)
        file.write("\n")
        
    team_rank=round((b_rank_avg+bo_rank_avg+a_rank_avg)/192*100/2,0)
    print '\n'
    print '\n'
    file.write('final team rank\n')
    print 'final team rank'
    print team_rank
    file.write(str(team_rank))