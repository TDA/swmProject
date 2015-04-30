import MySQLdb as mdb
import scipy.stats as ss
def calculateRank(data,index,order,name):
    newlist = list()
    if order==0 : 
        for i in data:
            if float(i[index])==0: newlist.append(10000)
            else: newlist.append(float(i[index]))
    else: newlist = [-float(i[index]) for i in data[0:]]
    rank = ss.rankdata(newlist,method='min')
    data[0].append(name)
    j=0
    for i in data[0:]:    
        i.append(rank[j])
        j=j+1
def getopenconnection(host='localhost', user='root', password='jaswi!23', dbname='swmproject'):
    return mdb.connect(host=host,  # your host, usually localhost
                           user=user,  # your username
                           passwd=password,  # your password
                           db=dbname)  # name of the data base

db= getopenconnection()
print db
maindata=[]
cur= db.cursor()
query = "select * from bowlers_attr"
cur.execute(query)
final =[ list(i) for i in cur] 
calculateRank(final,11,-1,"bowling_rank")
print final
for i in final:
    query1= "UPDATE bowler_attrs SET bowling_rank = '"+str(i[-1])+"' WHERE player_id = '"+str(i[1])+"'"
    cur.execute(query1)
db.commit()    